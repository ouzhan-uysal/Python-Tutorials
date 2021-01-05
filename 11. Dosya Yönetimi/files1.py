"""
Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
Kullanımı: open(dosya_adi, dosya_erişme_modu)
dosya_erişme_modu   => dosyayı hangi amaçla açtımızı belirtir. (Okuma, yazma, ekleme vs)

Erişim Modları:
"w" : (Write)   Yazma modu.     Dosyayı konumda oluşturur. Eğer önceden dosya varsa ondaki bilgiler silinir.
"a" : (Append)  Ekleme modu.    Dosya konumda yoksa oluşturur.
"x" : (Create)  Oluşturma modu. Dosya zaten varsa hata verir.
"r" : (Read)    Okuma modu.     Dosya konumda yoksa hata verir. Varsayılan erişim modudur.
"""

# 1
# f1 = open("newfile.txt", "w")   # Burada result'a aktarmamızın nedeni dosyaya bir referans eklemek istememizden. Bu referans sayesinde dosya üzerinden işlemler yapılabilir.
# f1.close()   # dosyanın açık kalıp kaynak tüketmesine izin vermemek için dosyayı kapatmak gerekir.
# print(f1)

# 2
# f2 = open("D:/newfile.txt", "w" encoding="utf-8") # Farklı bir dizinde dosya açma, encoding: Türkçe karakterleri tanıması için
# f2.close()
# print(f2)

# 3
# f3 = open("newfile.txt", "a", encoding="utf-8")  # Var olan dosyaya ekleme yapar
# f3.write("Oğuzhan Uysal\n")
# f3.close()

# 4
f4 = open("newfile.txt", "x", encoding="utf-8")  # Sadece dosya oluşturur. close yapmaya gerek yoktur.
f4.write("Oğuzhan Uysal ")   # Oluşan dosyanın içine direk yazar.