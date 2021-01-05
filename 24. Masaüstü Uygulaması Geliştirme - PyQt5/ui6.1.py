# ui6.py 'dan türetilen sınıf

import sys
import mysql.connector

from PyQt5 import QtWidgets
from ui6 import Ui_MainWindow

"""
# Ad, Soyad, Tel, E-Posta, Şifre, Plaka, İl, İlçe, Semt/Mahalle bilgilerini Database'e göderimi.
def db_gonder(self, name, surname, phone, password, email, license_plate, city, district, region):
    self.name = name
    self.surname = surname
    self.phone = phone
    self.password = password
    self.email = email
    self.license_plate = license_plate
    self.city = city
    self.district = district
    self.region = region

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "OPSdatabase1!",
        database = "ops-users"
    )
    # print(connection)
    cursor = connection.cursor()

    # Girilen Plaka sistemde kayıtlı olup olmadığını kontrol et.
    sql_where_lp = "Select license_plate From Users Where license_plate=%s"
    sql_where_lp_value = (self.license_plate,)
    cursor.execute(sql_where_lp, sql_where_lp_value)

    users = cursor.fetchone()

    plusCode4Digits = f"{district}+{region}"        # Bunun için bir program daha yazılmalı.
    residence_location = f'{city}/{plusCode4Digits}'

    if users == None:   # Plaka sistemde kayıtlı değilse plakanın kaydı
        sql_insert = "INSERT INTO Users(name, surname, phone, password, email, license_plate, residence_location) VALUES (%s,%s,%s,%s,%s,%s)"
        sql_insert_values = (self.name, self.surname, self.phone, self.email, self.password, self.license_plate,)

        cursor.execute(sql_insert, sql_insert_values)

        try:
            connection.commit()     # Verileri database'e gönderme işlemi burada başlar

        except mysql.connector.Error as err:
            print("Hata: ", err)

        finally:
            connection.close()      # Bağlantının kapatılması
            print("Database Bağlantısı Kesildi.")
    

    else:       # Plakanın sistemde kayıtlı olması durumu
        # Önce kayıtlı plakanın id'sini bulup o id'ye kullanıcı bilgilerinin giriş işlemleri başlatılacak.
        sql_insert = "INSERT INTO Users(name, surname, phone, password, email, residence_location) VALUES (%s,%s,%s,%s,%s)"
        sql_insert_values = (self.name, self.surname, self.phone, self.email, self.password,)
"""

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()   # Burada __init__
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_register.clicked.connect(self.islem)        # Register butonunun aktif edilmesi

    def islem(self):
        sender = self.sender().text()
        print(sender)
        if sender == "KAYIT OL":
            print(f"Ad\t: {self.ui.line_name.text()}\nSoyad\t: {self.ui.line_surname.text()}\nTelefon\t: {self.ui.line_phone.text()}\nE-Posta\t: {self.ui.line_email.text()}\nŞifre\t: {self.ui.line_password.text()}\nPlaka\t: {self.ui.line_license_plate.text()}\nŞehir\t: {self.ui.comboBox_city.currentText()}\nİlçe\t: {self.ui.comboBox_district.currentText()}\nSemt/Mahalle\t: {self.ui.comboBox_region.currentText()}\n")
        else:
            print("Hata")
    """
    def db_kaydet(self):
        sender = self.sender().text()
        if sender.text() == "Kayıt Ol":
            pass
    """

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()