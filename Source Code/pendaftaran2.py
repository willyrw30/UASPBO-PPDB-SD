from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox


class Pendaftaran(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1107, 912)
        self.lineEdit_nama_lengkap = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nama_lengkap.setGeometry(QtCore.QRect(230, 180, 801, 31))
        self.lineEdit_nama_lengkap.setObjectName("lineEdit_nama_lengkap")
        self.lineEdit_nama_ayah = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nama_ayah.setGeometry(QtCore.QRect(230, 320, 801, 31))
        self.lineEdit_nama_ayah.setObjectName("lineEdit_nama_ayah")
        self.lineEdit_nama_ibu = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nama_ibu.setGeometry(QtCore.QRect(230, 400, 801, 31))
        self.lineEdit_nama_ibu.setObjectName("lineEdit_nama_ibu")
        self.lineEdit_asal_sekolah = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_asal_sekolah.setGeometry(QtCore.QRect(230, 480, 801, 31))
        self.lineEdit_asal_sekolah.setObjectName("lineEdit_asal_sekolah")
        self.nama_lengkap = QtWidgets.QLabel(Dialog)
        self.nama_lengkap.setGeometry(QtCore.QRect(230, 160, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nama_lengkap.setFont(font)
        self.nama_lengkap.setObjectName("nama_lengkap")
        self.asal_sekolah = QtWidgets.QLabel(Dialog)
        self.asal_sekolah.setGeometry(QtCore.QRect(230, 460, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.asal_sekolah.setFont(font)
        self.asal_sekolah.setObjectName("asal_sekolah")
        self.nama_ayah = QtWidgets.QLabel(Dialog)
        self.nama_ayah.setGeometry(QtCore.QRect(230, 300, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nama_ayah.setFont(font)
        self.nama_ayah.setObjectName("nama_ayah")
        self.nama_ibu = QtWidgets.QLabel(Dialog)
        self.nama_ibu.setGeometry(QtCore.QRect(230, 370, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nama_ibu.setFont(font)
        self.nama_ibu.setObjectName("nama_ibu")
        self.alamat = QtWidgets.QLabel(Dialog)
        self.alamat.setGeometry(QtCore.QRect(230, 530, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.alamat.setFont(font)
        self.alamat.setObjectName("alamat")
        self.pushButton_simpan = QtWidgets.QPushButton(Dialog)
        self.pushButton_simpan.setGeometry(QtCore.QRect(230, 740, 93, 28))
        self.pushButton_simpan.setObjectName("pushButton_simpan")
        self.pushButton_batal = QtWidgets.QPushButton(Dialog)
        self.pushButton_batal.setGeometry(QtCore.QRect(340, 740, 93, 28))
        self.pushButton_batal.setObjectName("pushButton_batal")
        self.textEdit_alamat = QtWidgets.QTextEdit(Dialog)
        self.textEdit_alamat.setGeometry(QtCore.QRect(230, 560, 811, 171))
        self.textEdit_alamat.setObjectName("textEdit_alamat")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(400, 10, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_usia = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_usia.setGeometry(QtCore.QRect(230, 250, 801, 31))
        self.lineEdit_usia.setObjectName("lineEdit_usia")
        self.usia = QtWidgets.QLabel(Dialog)
        self.usia.setGeometry(QtCore.QRect(230, 230, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usia.setFont(font)
        self.usia.setObjectName("usia")
        self.pushButton_kembali = QtWidgets.QPushButton(Dialog)
        self.pushButton_kembali.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        self.lineEdit_nomor_pendafaran = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nomor_pendafaran.setGeometry(
            QtCore.QRect(230, 100, 801, 31))
        self.lineEdit_nomor_pendafaran.setText("")
        self.lineEdit_nomor_pendafaran.setObjectName(
            "lineEdit_nomor_pendafaran")
        self.nomor_pendaftaran = QtWidgets.QLabel(Dialog)
        self.nomor_pendaftaran.setGeometry(QtCore.QRect(230, 80, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomor_pendaftaran.setFont(font)
        self.nomor_pendaftaran.setObjectName("nomor_pendaftaran")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nama_lengkap.setText(_translate("Dialog", "NAMA LENGKAP :"))
        self.asal_sekolah.setText(_translate("Dialog", "ASAL SEKOLAH :"))
        self.nama_ayah.setText(_translate("Dialog", "NAMA AYAH :"))
        self.nama_ibu.setText(_translate("Dialog", "NAMA IBU :"))
        self.alamat.setText(_translate("Dialog", "ALAMAT :"))
        self.pushButton_simpan.setText(_translate("Dialog", "SIMPAN"))
        self.pushButton_batal.setText(_translate("Dialog", "BATAL"))
        self.label_7.setText(_translate("Dialog", "PENDAFTARAN SISWA"))
        self.usia.setText(_translate("Dialog", "USIA :"))
        self.pushButton_kembali.setText(_translate("Dialog", "KEMBALI"))
        self.nomor_pendaftaran.setText(
            _translate("Dialog", "Nomor Pendaftaran:"))
        self.pushButton_simpan.clicked.connect(self.simpanData)

    def simpanData(self):
        nomor_pendaftaran = self.lineEdit_nomor_pendafaran.text()
        nama_lengkap = self.lineEdit_nama_lengkap.text()
        asal_sekolah = self.lineEdit_asal_sekolah.text()
        nama_ayah = self.lineEdit_nama_ayah.text()
        nama_ibu = self.lineEdit_nama_ibu.text()
        alamat = self.textEdit_alamat.toPlainText()
        usia = self.lineEdit_usia.text()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ppdb'
            )

            cursor = connection.cursor()

            sql = """
                INSERT INTO pendaftaran (id_pendaftaran,nama_siswa,usia, nama_ayah, nama_ibu,asal_sekolah,alamat_siswa)
                VALUES (%s,%s, %s, %s, %s, %s, %s)
            """
            val = (nomor_pendaftaran, nama_lengkap, usia,
                   nama_ayah, nama_ibu, asal_sekolah, alamat)

            cursor.execute(sql, val)
            connection.commit()

            QMessageBox.information(
                None, "Success", "Data berhasil disimpan ke database")

        except mysql.connector.Error as error:
            if "1062" in str(error):
                QMessageBox.warning(
                    None, "Duplicate Entry", "Nomor pendaftaran sudah ada dalam database")
            else:
                print("Gagal menyimpan data:", error)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Pendaftaran()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
