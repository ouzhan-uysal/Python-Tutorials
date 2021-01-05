# MySQL: Delete Sorgusu => Kayıt Silme

import mysql.connector

def deleteUser(license_plate):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "OPSdatabase1!",
        database = "ops-users"
    )
    # print(connection)

    cursor = connection.cursor()

    # Alttaki satırı sadece "delete from users" olarak yazarsan tüm tablolar silinir.
    sql_del = "Delete from Users where license_plate=%s"
    sql_del_value = (license_plate,)
    cursor.execute(sql_del, sql_del_value)

    try:
        connection.commit()
        print("Kayıt Silindi.")

    except mysql.connector.Error as err:
        print("Hata: ", err)

    finally:
        print("Database Bağlantısı Sonlandırıldı.")


deleteUser("52SOFG32")