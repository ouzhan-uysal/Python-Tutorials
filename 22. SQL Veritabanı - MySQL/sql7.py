# MySQL Update => Kayıt Güncelleme

import mysql.connector

def updateUser(license_plate, last_seen_location):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "OPSdatabase1!", database = "ops-users")
    # print(connection)
    cursor = connection.cursor()
    
    sql_insert = "UPDATE Users Set last_seen_location=%s where license_plate=%s"
    sql_insert_values = (last_seen_location, license_plate,)

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


updateUser("32SOFG32","34/7EDZ+MS")