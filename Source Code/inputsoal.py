import sys
import mysql.connector
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox


class InputSoal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1101, 853)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(140, 30, 721, 61))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.soal = QtWidgets.QLabel(Form)
        self.soal.setGeometry(QtCore.QRect(70, 120, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soal.setFont(font)
        self.soal.setObjectName("soal")
        self.pilihan_a = QtWidgets.QLabel(Form)
        self.pilihan_a.setGeometry(QtCore.QRect(70, 240, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pilihan_a.setFont(font)
        self.pilihan_a.setObjectName("pilihan_a")
        self.pilihan_b = QtWidgets.QLabel(Form)
        self.pilihan_b.setGeometry(QtCore.QRect(70, 360, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pilihan_b.setFont(font)
        self.pilihan_b.setObjectName("pilihan_b")
        self.pilihan_c = QtWidgets.QLabel(Form)
        self.pilihan_c.setGeometry(QtCore.QRect(70, 480, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pilihan_c.setFont(font)
        self.pilihan_c.setObjectName("pilihan_c")
        self.pushButton_simpan = QtWidgets.QPushButton(Form)
        self.pushButton_simpan.setGeometry(QtCore.QRect(70, 790, 111, 51))
        self.pushButton_simpan.setObjectName("pushButton_simpan")
        self.pushButton_2_batal = QtWidgets.QPushButton(Form)
        self.pushButton_2_batal.setGeometry(QtCore.QRect(190, 790, 111, 51))
        self.pushButton_2_batal.setObjectName("pushButton_2_batal")
        self.Jawaban = QtWidgets.QLabel(Form)
        self.Jawaban.setGeometry(QtCore.QRect(70, 670, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Jawaban.setFont(font)
        self.Jawaban.setObjectName("Jawaban")
        self.textEdit_soal = QtWidgets.QTextEdit(Form)
        self.textEdit_soal.setGeometry(QtCore.QRect(70, 140, 781, 91))
        self.textEdit_soal.setObjectName("textEdit_soal")
        self.textEdit_pilihan_a = QtWidgets.QTextEdit(Form)
        self.textEdit_pilihan_a.setGeometry(QtCore.QRect(70, 260, 781, 91))
        self.textEdit_pilihan_a.setObjectName("textEdit_pilihan_a")
        self.textEdit_pilihan_b = QtWidgets.QTextEdit(Form)
        self.textEdit_pilihan_b.setGeometry(QtCore.QRect(70, 380, 781, 91))
        self.textEdit_pilihan_b.setObjectName("textEdit_pilihan_b")
        self.textEdit_pilihan_c = QtWidgets.QTextEdit(Form)
        self.textEdit_pilihan_c.setGeometry(QtCore.QRect(70, 500, 781, 91))
        self.textEdit_pilihan_c.setObjectName("textEdit_pilihan_c")
        self.textEdit_jawaban = QtWidgets.QTextEdit(Form)
        self.textEdit_jawaban.setGeometry(QtCore.QRect(70, 690, 781, 91))
        self.textEdit_jawaban.setObjectName("textEdit_jawaban")
        self.point = QtWidgets.QLabel(Form)
        self.point.setGeometry(QtCore.QRect(70, 600, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.point.setFont(font)
        self.point.setObjectName("point")
        self.lineEdit_poin = QtWidgets.QLineEdit(Form)
        self.lineEdit_poin.setGeometry(QtCore.QRect(70, 620, 211, 41))
        self.lineEdit_poin.setObjectName("lineEdit_poin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Sambungkan fungsi simpan ke tombol "Simpan"
        self.pushButton_simpan.clicked.connect(self.simpan)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "PEMBUAT SOAL"))
        self.soal.setText(_translate("Form", "Soal"))
        self.pilihan_a.setText(_translate("Form", "Pilihan A"))
        self.pilihan_b.setText(_translate("Form", "Pilihan B"))
        self.pilihan_c.setText(_translate("Form", "Pilihan C"))
        self.pushButton_simpan.setText(_translate("Form", "Simpan"))
        self.pushButton_2_batal.setText(_translate("Form", "Batal"))
        self.Jawaban.setText(_translate("Form", "Jawaban"))
        self.point.setText(_translate("Form", "Poin"))

    def simpan(self):
        question = self.textEdit_soal.toPlainText()
        option_a = self.textEdit_pilihan_a.toPlainText()
        option_b = self.textEdit_pilihan_b.toPlainText()
        option_c = self.textEdit_pilihan_c.toPlainText()
        point = self.lineEdit_poin.text()
        correct_answer = self.textEdit_jawaban.toPlainText()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ppdb'
            )
            cursor = conn.cursor()

            query = "INSERT INTO pertanyaan (pertanyaan, pilihan_a, pilihan_b, pilihan_c, poin, jawaban) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (question, option_a, option_b,
                    option_c, point, correct_answer)

            cursor.execute(query, data)
            conn.commit()
            QMessageBox.information(
                None, 'Sukses', 'Pertanyaan berhasil dimasukkan ke dalam database')

            conn.close()
        except mysql.connector.Error as error:
            QMessageBox.critical(
                None, 'Error', f'Gagal memasukkan pertanyaan ke dalam database: {error}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = InputSoal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
