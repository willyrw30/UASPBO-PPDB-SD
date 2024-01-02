from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class HasilSeleksi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 852)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(35, 81, 1061, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)  # Mengatur jumlah kolom
        self.tableWidget.setHorizontalHeaderLabels(
            ["Nama Siswa", 'nama_ayah', "Usia", "Skor"])  # Label kolom
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)  # Menyesuaikan ukuran kolom

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 640, 241, 51))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(912, 30, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.tampilkanData)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Tampilkan"))
        self.comboBox.setItemText(0, _translate("Dialog", "Diterima"))
        self.comboBox.setItemText(1, _translate("Dialog", "Tidak Diterima"))

    def tampilkanData(self):
        try:
            self.db = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='ppdb'
            )
            print("Koneksi ke database berhasil")
        except mc.Error as e:
            print("Tidak bisa terhubung ke database:", e)

        status = self.comboBox.currentText()
        cursor = self.db.cursor()

        if status == "Diterima":
            query = "SELECT nama_siswa, nama_ayah, usia, skor FROM pendaftaran INNER JOIN hasil_kuis ON pendaftaran.id_pendaftaran = hasil_kuis.id_pendaftaran WHERE status_penerimaan='Diterima'"
        else:
            query = "SELECT nama_siswa, nama_ayah, usia, skor FROM pendaftaran INNER JOIN hasil_kuis ON pendaftaran.id_pendaftaran = hasil_kuis.id_pendaftaran WHERE status_penerimaan='Tidak Diterima'"

        cursor.execute(query)

        # Mengosongkan tableWidget sebelum menampilkan data baru
        self.tableWidget.setRowCount(0)

        # Memasukkan data dari database ke tableWidget
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.tableWidget.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_index, col_index, item)

        cursor.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = HasilSeleksi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
