# MySQL: Select/Get Sorgusu: Veritabanından veriyi çekme / verinin olup olmadığını kontrol etme.

import mysql.connector

class veriCekme:
    def __init__(self, license_plate):
        self.license_plate = license_plate

        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "OPSdatabase1!",
            database = "ops-users"
        )
        # print(connection)

        self.cursor = self.connection.cursor()

    def getUsers(self):

        self.cursor.execute("Select * From Users")

        users = self.cursor.fetchall()

        for u in users:
            print(u)

    def getUser(self):

        sql_get = "SELECT license_plate, debt From Users where license_plate=%s"
        sql_get_values = (self.license_plate, )
        self.cursor.execute(sql_get, sql_get_values)
        

        lp = self.cursor.fetchone()
        
        if lp != None:
            print("Plaka Sistemde Kayıtlı")
            print(f"Plaka: {lp[0]}\nPlakanın Borcu: {lp[1]}")
        elif lp == None:
            print("Yeni Araç")
        
        
        # lp = self.cursor.fetchall()      #fetchall(): Bulduğu tüm kayıtları getirir. fetchone(): Bulduğu ilk kayıdı getirir.
        # for l in lp:
        #     if l[0] == self.license_plate:
        #         print("Plaka Sistemde Kayıtlı")


# getUsers()
g1 = veriCekme("32SOFG32")
g1.getUser()
# veriCekme.getUser("32SOFG32")