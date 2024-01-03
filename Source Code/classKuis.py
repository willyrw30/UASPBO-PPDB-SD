import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QInputDialog
from PyQt5 import QtWidgets


class ResultWindow(QWidget):
    def __init__(self, result_text, participant_id, correct_answers):
        super().__init__()

        self.setWindowTitle('Hasil Kuis')
        self.setGeometry(200, 200, 300, 200)

        self.result_label = QLabel(result_text)
        self.akhiri = QPushButton('Selesai')

        self.participant_id = participant_id
        self.correct_answers = correct_answers

        self.akhiri.clicked.connect(self.save_and_close)

        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.akhiri)
        self.setLayout(layout)

    def save_and_close(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        insert_query = "INSERT INTO hasil_kuis (id_pendaftaran, skor) VALUES (%s, %s)"
        cursor.execute(
            insert_query, (self.participant_id, self.correct_answers))

        conn.commit()
        conn.close()

        QMessageBox.information(
            self, 'Simpan ke Database', 'Hasil kuis telah disimpan ke database.')

        QApplication.instance().quit()
