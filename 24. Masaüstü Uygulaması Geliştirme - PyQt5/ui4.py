# Calculater

import sys
from PyQt5 import QtWidgets     # Form elemanlarının hepsini QtWidgets'ten çekiyoruz
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1: ")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
        
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2: ")
        self.lbl_sayi2.move(50,60)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,60)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,100)
        self.btn_topla.resize(200,32)
        self.btn_topla.clicked.connect(self.islem)
        
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(150,133)
        self.btn_cikar.resize(200,32)
        self.btn_cikar.clicked.connect(self.islem)
        
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(150,166)
        self.btn_carp.resize(200,32)
        self.btn_carp.clicked.connect(self.islem)
        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(150,199)
        self.btn_bol.resize(200,32)
        self.btn_bol.clicked.connect(self.islem)

        self.result = QtWidgets.QLabel(self)
        self.result.setText("Sonuç: ")
        self.result.move(150, 232)
        self.result.resize(200,32)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.setText("Çıkış")
        self.btn_exit.move(150, 300)
        self.btn_exit.resize(200,32)
        self.btn_exit.clicked.connect(self.islem)

    """
    def toplama(self):
        self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())))

    def cikarma(self):
        self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())))
    
    def carpma(self):
        self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())))
    
    def bolme(self):
        self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())))

    def cikis(self):
        sys.exit(0)
    """
    # Aşağıdaki islem metodu yukarıdaki 4 sınıfın işlevini yerine getirir.
    def islem(self):
        sender = self.sender()  # hangi butona tıklanırsa ilgili obje içerisinden bu olayın referansını alır.
        # print(sender.text())  # Hangi butona basıldığını yazdırır.
        r = 0

        if sender.text() == "Topla":
            self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())))

        elif sender.text() == "Çıkar":
            self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())))

        elif sender.text() == "Çarp":
            self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())))

        elif sender.text() == "Böl":
            self.result.setText("Sonuç: "+ str(int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())))

        elif sender.text() == "Çıkış":
            sys.exit(0)


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()