# Raising an Exception  => Hata Nesnesi Oluşturma

# Girilen veri türlerinin doğru olması fakat bizim istediğimiz aralıkta olmaması durumunda kendimizin oluşturduğu exceptinlar

def check_password(psw):
    import re   # Regular Expressions: kontrol işlemleri yapmak için kullandık.

    if len(psw) < 8:
        raise Exception("parola en az 8 karakter olmalıdır.")
    
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir.")
    
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir.")
    
    elif not re.search("[!'^+%&/()=?*]", psw):
        raise Exception("parola numeric karakter içermelidir.")
    
    elif re.search("\s", psw):
        raise Exception("parola boşluk içermemelidir.")

    else:
        print("Geçerli Parola")

password = "12345678aB!"

try:
    check_password(password)
except Exception as e:
    print(e)
else:
    print("Validation Completed.")