# MySQL: Insert Sorgusu => Kayıt ekleme

import mysql.connector

def insertUser(license_plate, last_seen_location):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "OPSdatabase1!",
        database = "ops-users"
    )
    # print(connection)

    cursor = connection.cursor()
    sql_insert = "INSERT INTO Users(license_plate, last_seen_location) VALUES (%s,%s)"
    sql_insert_values = (license_plate, last_seen_location,)

    cursor.execute(sql_insert, sql_insert_values)

    try:
        connection.commit()     # Verileri database'e gönderme işlemi burada başlar
        print(f'{cursor.rowcount}')     # Kaç tane kayıt eklendiğini gösterir.
        print(f'Son Eklenen Kaydın ID: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print("Hata: ", err)

    finally:
        connection.close()      # Bağlantının kapatılması
        print("Database Bağlantısı Kesildi.")


insertUser("12SOFG32", "34/XYZ1+MC")