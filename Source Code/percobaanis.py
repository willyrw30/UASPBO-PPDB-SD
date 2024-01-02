import sys
from PyQt5 import QtCore, QtGui
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QMessageBox


class InputSeleksi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName('Penerimaan Siswa')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'Nama', 'Usia', 'Penerimaan'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.btn_hasil = QPushButton('Lihat Hasil Seleksi')
        self.btn_hasil.clicked.connect(self.perform_selection)
        self.layout.addWidget(self.btn_hasil)

        self.refresh_table()

    def perform_selection(self):
        self.update_acceptance_based_on_age()
        self.refresh_table()
        QMessageBox.information(
            self, 'Info', 'Hasil seleksi telah diperbarui!')

    def refresh_table(self):
        self.table.setRowCount(0)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ppdb"
        )

        mycursor = mydb.cursor()

        mycursor.execute(
            "SELECT id_pendaftaran, nama_siswa, usia, status_penerimaan FROM pendaftaran")
        data = mycursor.fetchall()

        for row_number, row_data in enumerate(data):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.table.setItem(row_number, column_number, item)

        mycursor.close()

    def update_acceptance_based_on_age(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ppdb"
        )

        mycursor = mydb.cursor()

        mycursor.execute(
            "SELECT id_pendaftaran, usia FROM pendaftaran")
        data = mycursor.fetchall()

        for row_data in data:
            id_pendaftaran = row_data[0]
            usia = int(row_data[1])

            if usia < 7:
                status_penerimaan = 'Tidak Diterima'
            else:
                status_penerimaan = 'Diterima'

            mycursor.execute("UPDATE pendaftaran SET status_penerimaan = %s WHERE id_pendaftaran = %s",
                             (status_penerimaan, id_pendaftaran))

        mydb.commit()
        mycursor.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = InputSeleksi()
    ui.show()
    sys.exit(app.exec_())
