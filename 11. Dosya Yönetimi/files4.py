# Öğrenci Kayıt Programı - Demo

def not_hesapla(satir):
    satir = satir[:-1]  # satirin sonunda oluşan boşluk silinir
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = str((not1+not2+not3)/3)

    return ogrenciAdi + " : " + ortalama + "\n"


def ort_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as sn:
        for satir in sn:
            print(not_hesapla(satir))

def not_gir():
    ad = input("İsim Giriniz")
    soyad = input("Soyad Giriniz")
    not1 = input("1. Notu Giriniz")
    not2 = input("2. Notu Giriniz")
    not3 = input("3. Notu Giriniz")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as sn:
        sn.writelines(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")

def not_kaydet():
    pass

while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4-Çıkış\n")

    if islem == '1':
        ort_oku()

    elif islem == '2':
        not_gir()
    
    elif islem == '3':
        not_kaydet()

    elif islem == '4':
        break

    else:
        print("Hatalı Giriş")