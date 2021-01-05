# OPS MySQL Database

import mysql.connector

class mysqlDatabase:
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


    def get_LP_Debt(self):  # Burada sadece license_plate parametresi kullanılacak.
        # Gelen plaka sistemde kayıtlı mı değil mi kontrol işlemi
        sql_where_lp = "SELECT license_plate, debt From Users Where license_plate=%s"
        sql_where_lp_value = (self.license_plate,)
        self.cursor.execute(sql_where_lp, sql_where_lp_value)

        lp = self.cursor.fetchone()

        if lp == None:  # Plaka sistemde kayıtlı değilse borcuda 0.0'dır.
            return 0.0

        else:       # Plakanın sistemde kayıtlı olması durumundan güncel borcunun getirilmesi
            return lp[1]



    def update_LP_Debt(self, last_seen_location, parking_fee):
        # Gelen plaka sistemde kayıtlı mı değil mi kontrol işlemi
        sql_where_lp = "SELECT license_plate From Users Where license_plate=%s"
        sql_where_lp_value = (self.license_plate,)
        self.cursor.execute(sql_where_lp, sql_where_lp_value)

        lp = self.cursor.fetchone()

        if lp == None:   # Plaka sistemde kayıtlı değilse plakanın kaldığı süresinin ücretiyle beraber kaydı
            print("Yeni Araç Plakası")
            # Aracın plakayla beraber debt'in kaydedilmesi
            sql_insert = "INSERT INTO Users(license_plate, debt, last_seen_location) VALUES (%s,%s,%s)"
            sql_insert_values = (self.license_plate, parking_fee, last_seen_location,)
            self.cursor.execute(sql_insert, sql_insert_values)

            try:
                print(f'Son Eklenen Kaydın ID: {self.cursor.lastrowid}')
                self.connection.commit()     # Verileri database'e gönderme işlemi burada başlar

            except mysql.connector.Error as err:
                print("Hata: ", err)

            finally:
                self.connection.close()      # Bağlantının kapatılması
                print("Database Bağlantısı Kesildi.")
        

        else:       # Plakanın sistemde kayıtlı olması durumunda. Borcunun güncellenmesi
            print("Araç Sistemde Kayıtlı")
            sql_update = "UPDATE Users Set debt=%s, last_seen_location=%s Where license_plate=%s"
            sql_update_values = (parking_fee, last_seen_location, self.license_plate,)
            self.cursor.execute(sql_update, sql_update_values)

            try:
                self.connection.commit()     # Verileri database'e gönderme işlemi burada başlar
                print(f'Son Eklenen Kaydın ID: {self.cursor.lastrowid}')

            except mysql.connector.Error as err:
                print("Hata: ", err)

            finally:
                self.connection.close()      # Bağlantının kapatılması
                print("Database Bağlantısı Kesildi.")


# print(mysqlDatabase("02SOFG32").get_LP_Debt())
print(mysqlDatabase("08SOFG32").update_LP_Debt("34/ABCD+XY", "10.5"))     # Parametreler: Plaka, Şehir kodu, park pluscode