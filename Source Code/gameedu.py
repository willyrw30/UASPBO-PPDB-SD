from PyQt5 import QtCore, QtGui, QtWidgets
from puzzle.game15 import MainWindow
import sys


class Ui_GameEdukatif(object):
    def setupUi(self, GameEdukatif):
        GameEdukatif.setObjectName("GameEdukatif")
        GameEdukatif.resize(227, 128)
        self.horizontalLayoutWidget = QtWidgets.QWidget(GameEdukatif)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 195, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(GameEdukatif)
        QtCore.QMetaObject.connectSlotsByName(GameEdukatif)

    def retranslateUi(self, GameEdukatif):
        _translate = QtCore.QCoreApplication.translate
        GameEdukatif.setWindowTitle(
            _translate("GameEdukatif", "Game Edukatif"))
        self.pushButton_2.setText(_translate("GameEdukatif", "Puzzle"))

        def InputSoalWindow():
            self.inputSoal_ui = MainWindow()

        self.pushButton_2.clicked.connect(InputSoalWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GameEdukatif = QtWidgets.QWidget()
    ui = Ui_GameEdukatif()
    ui.setupUi(GameEdukatif)
    GameEdukatif.show()
    sys.exit(app.exec_())
