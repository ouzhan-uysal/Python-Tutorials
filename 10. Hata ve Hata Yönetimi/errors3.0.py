# Error Handling Demo

liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

"""
Şartlar:
    1: Liste elemanları içindeki sayısal değerleri bulunuz.

    2: Kullanıcı 'q' değerinin girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

    3: Girilen parola içinde türkçe karakter hatası veriniz.

    4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
"""

class check_list:
    def __init__(self, liste):
        for i in liste:
            try:
                result = int(i)
                print(result)

            except ValueError:
                continue


while True:
    deger = input("Çıkış yapmak için 'q' değerini girin.\n")
    if deger == 'q':
        break
    else:
        check_list(liste)   # listenin kontrolü