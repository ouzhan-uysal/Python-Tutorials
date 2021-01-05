# MySQL: Order By Sorgusu => Kayıt Sıralama

import mysql.connector

def getUsers():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "OPSdatabase1!",
        database = "ops-users"
    )
    # print(connection)

    cursor = connection.cursor()

    cursor.execute("Select * From Users Order By id")   # Bu şekilde 1 den başlayıp sıralayacak. id'nin sonuna boşluk bırakıp DESC ifadesini yazarsak bu sefer tersten sıralar.
                                                        # Eğer id, name şeklinde yazılırsa önce id'ye göre sonrasında name'e göre sıralama yapar.

    users = cursor.fetchall()

    for u in users:
        print(u)


getUsers()