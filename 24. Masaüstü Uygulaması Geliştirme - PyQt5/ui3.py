import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip

class MyWindow(QMainWindow):        #QMainWindow'dan pencere üretme
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Third Window")
        self.setGeometry(600, 300, 640, 480)
        self.setToolTip("On The Window")
        self.initIU()

    def initIU(self):
        self.lbl_name = QtWidgets.QLabel(self)  # pen üzerinden yeni bir label oluşturma.
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50, 30)  # label'ı hareket ettirme
        self.lbl_surname = QtWidgets.QLabel(self)  # label soyad
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50, 70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Sonuç: ")
        self.lbl_result.resize(300,200)
        self.lbl_result.move(100, 150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(100, 30)
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(100, 70)
        
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(100, 110)
        self.btn_save.clicked.connect(self.tiklanma)

    def tiklanma(self):
        self.lbl_result.setText(f"Ad\t: {self.txt_name.text()}\nSoyad\t: {self.txt_surname.text()}")



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()