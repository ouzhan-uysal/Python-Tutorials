# Kayıt Filtreleme: Where Sorgusu

import mysql.connector

def getUser(license_plate):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "OPSdatabase1!",
        database = "ops-users"
    )
    # print(connection)

    cursor = connection.cursor()
    
    """
    Where name="Samsung"        : Direk adı Samsung olan kayıtları getirir.
    Where name LIKE '%Samsung%' : Adı içerisinde Samsung olan kayıtları getirir.
    # Bu işlemlerin arasına or veya and operatörleri konularak birden fazla filtre eklenebilir. Örn: name="Samsung" and price="3600" gibi
    """

    sql_where_lp = "Select license_plate From Users Where license_plate=%s"
    sql_where_lp_value = (license_plate,)
    cursor.execute(sql_where_lp, sql_where_lp_value)

    users = cursor.fetchone()

    if users == None:
        print("Yeni Plaka Kayıt İşlemi Yapılacak.")
    
    elif users[0] == license_plate:
        print("Araç Sistemde Kayıtlı")
        
    else:
        print("Buraya girmez herhalde.")


getUser("32xOFG32")