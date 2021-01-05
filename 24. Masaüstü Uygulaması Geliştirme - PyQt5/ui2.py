"""
QLabel
QComboBox
QCheckBox
QRadioButton
QPushButton
QTableWidget
QLineEdit
QSlider
QProgressBar
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip
from PyQt5.QtGui import QIcon


def pencere():
    app = QApplication(sys.argv)
    pen = QMainWindow()

    pen.setWindowTitle("Second Window")
    pen.setGeometry(600, 300, 640, 480)
    pen.setToolTip("On The Window")

    lbl_name = QtWidgets.QLabel(pen)  # pen üzerinden yeni bir label oluşturma.
    lbl_name.setText("Adınız: ")
    lbl_name.move(50, 30)  # label'ı hareket ettirme
    lbl_surname = QtWidgets.QLabel(pen)  # label soyad
    lbl_surname.setText("Soyadınız: ")
    lbl_surname.move(50, 70)

    txt_name = QtWidgets.QLineEdit(pen)
    txt_name.move(100, 30)
    txt_surname = QtWidgets.QLineEdit(pen)
    txt_surname.move(100, 70)

    def tiklanma():
        print("Butona Tıklayan İsim: " + txt_name.text() + "\nSurname: " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(pen)
    btn_save.setText("Kaydet")
    btn_save.move(100, 110)
    btn_save.clicked.connect(tiklanma)



    pen.show()
    sys.exit(app.exec_())





pencere()
