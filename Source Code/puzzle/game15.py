import sys
import random
import threading
import time

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QGridLayout, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import mysql.connector
# from button import MyButton


class MainWindow(QWidget):
    nametxt = " Puzzle Angka Puzzle Angka "
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    winner = numbers[1:] + numbers[:1]
    attempts = 0

    def __init__(self):
        random.shuffle(self.numbers)
        super().__init__()
        self.grid = QGridLayout()
        self.layout = QVBoxLayout()
        self.name = QLabel(self.nametxt)
        self.name.setFont(QFont('Arial', 18))
        self.btnRestart = QPushButton("RESTART")

        self.participant_id = None  # Add this line to initialize participant_id

        self.buttons = [MyButton(i) for i in self.numbers]
        self.positions = [(i, j) for i in range(4) for j in range(4)]

        for btn, pos in zip(self.buttons, self.positions):
            btn.position = list(pos)
            self.grid.addWidget(btn, *pos)
            btn.clicked.connect(self.btn_clicked)

        self.btnRestart.clicked.connect(self.restart)
        threading.Thread(target=self.runner_title).start()

        self.layout.addWidget(self.btnRestart)
        self.layout.addWidget(self.name)
        self.layout.addLayout(self.grid)

        self.setLayout(self.layout)
        self.show()
        self.masukkan_id()

    def masukkan_id(self):
        while True:
            participant, ok_pressed = QInputDialog.getText(
                self, 'Masukkan ID Peserta', 'ID Peserta:')
            if ok_pressed:
                self.participant_id = participant
                if self.cek_peserta() and not self.repeat_test():
                    break
                else:
                    QMessageBox.warning(
                        self, 'ID Peserta Tidak Valid', 'ID Peserta tidak ditemukan atau Anda sudah melakukan kuis. Masukkan ID Peserta yang valid.')
            else:
                sys.close()

    def cek_peserta(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        participant_id = self.participant_id

        cursor.execute(
            "SELECT COUNT(*) FROM status_kuis WHERE id_pendaftaran = %s", (participant_id,))
        count = cursor.fetchone()[0]

        conn.close()

        return count > 0

    def repeat_test(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        participant_id = self.participant_id

        cursor.execute(
            "SELECT COUNT(*) FROM hasil_kuis WHERE id_pendaftaran = %s", (participant_id,))
        count = cursor.fetchone()[0]

        conn.close()

        return count > 0

    def btn_clicked(self):
        self.attempts += 1
        # self.tabriklation()
        btn = self.sender()
        for i in self.buttons:
            if i.value == 0 and (i.position[0] == btn.position[0] + 1 or i.position[0] == btn.position[0] - 1) and i.position[1] == btn.position[1]:
                btn.value, i.value = i.value, btn.value
                btn.setText(btn.value == 0)
                i.setText(i.value == 0)
            elif i.value == 0 and (i.position[1] == btn.position[1] + 1 or i.position[1] == btn.position[1] - 1) and i.position[0] == btn.position[0]:
                btn.value, i.value = i.value, btn.value
                btn.setText(btn.value == 0)
                i.setText(i.value == 0)

        self.checker()

    def restart(self):
        self.attempts = 0
        self.buttons.clear()
        random.shuffle(self.numbers)
        self.buttons = [MyButton(i) for i in self.numbers]
        for btn, pos in zip(self.buttons, self.positions):
            btn.position = list(pos)
            self.grid.addWidget(btn, *pos)
            btn.clicked.connect(self.btn_clicked)

    def checker(self):
        count = 0
        if self.buttons[15].value == 0:
            for i in range(16):
                if self.buttons[i].value == self.winner[i]:
                    count += 1
        if count >= 15:
            self.tabriklation()

    def tabriklation(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Selamat!")
        text = f"\nTotal Gerak {self.attempts}\nID Peserta: {
            self.participant_id}\n"  # Include participant_id in the message
        dlg.setText(text)
        dlg.setFont(QFont('Arial', 15))
        dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret = dlg.exec_()

        if ret == QMessageBox.Ok:
            self.insert_to_database()
            self.masukkan_id()
        else:
            sys.exit()

    def insert_to_database(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        query = "INSERT INTO hasil_puzzle (id_peserta, skor) VALUES (%s, %s)"
        values = (self.participant_id, self.attempts)

        cursor.execute(query, values)
        conn.commit()
        self.show_success_message()
        conn.close()

    def runner_title(self):
        txt = self.nametxt
        ln = len(txt)
        while True:
            txt = txt[1:] + txt[:1]
            self.name.setText(txt)
            time.sleep(0.15)

    def show_success_message(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Data Tersimpan")
        dlg.setText("Data telah berhasil disimpan ke dalam database.")
        dlg.setFont(QFont('Arial', 12))
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec_()


class MyButton(QPushButton):
    def __init__(self, value, position=None):
        super().__init__()

        self.setFixedSize(QSize(80, 80))
        self.setFont(QFont('Arial', 20))
        self.value = value
        self.position = position
        self.setText(False)

    def setText(self, click: bool):
        if self.value == 0:
            super().setText(f"")
        else:
            super().setText(f"{self.value}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = MainWindow()
    sys.exit(app.exec_())
