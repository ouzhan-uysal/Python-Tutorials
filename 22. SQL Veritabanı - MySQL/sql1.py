# MySQL Database Password: OPSdatabase1!

# MySQL - Python Bağlantısı için Pypi.org adresinden "mysql connector" kur.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",     # Local değilde online bir database'e bağlanırken localhost yerine => satın alınan server'ın IP Adresi buraya yazılır. Örn: 192.23.45.56
    user = "root",          # MySQL'e bağlanırken kullandığın id ve şifre:
    password = "OPSdatabase1!",
    database = "ops-users"  # Database'e bağlandıktan sonra hangi Shema üzerinde işlem yapılacağı belirtiyor.
)
# print(mydb)     # Bağlanıp bağlanamadığımızı görürüz.

mycursor = mydb.cursor()        # Kürsör oluşturduktan sonra database üzerinden işlemler yapılır. Şema oluşturma, tablo ekleme,silme,güncelleme vs.
# print(mycursor)
"""
# mycursor.execute("CREATE DATABASE mydatabase")  # Yeni bir Schema oluşturur.

mycursor.execute("SHOW DATABASES")  # Database'deki Schema'lara erişim.
for i in mycursor:      # Database'deki Shema'ları yazdırma.
    print(i)
"""

# mycursor.execute("CREATE TABLE cities(name VARCHAR(20), number_of_cams INT(10))")  # cities adlı bir tablo oluşturup, içerisine name ve number_of_cams adlı iki adet sütun oluşturma.