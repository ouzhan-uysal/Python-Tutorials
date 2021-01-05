# OS Modülü => İşletim sistemi, klasör, vs. hakkında bilgi edinebilir. Dosya işlemleri yapılabilir.
 
import os

# r = dir(os)   # os modülü içerisinde kullanılabilecek fonksiyonları gösterir.
# print(r)

# r = os.name   # İşletim sistemi hakkında bilgi verir. Windows ise nt çıktısı alırsın.
# print(r)

# os.chdir("C:\\")    # bulunduğun dizini değiştirmeni sağlar
# os.chdir("..")    # bir üst klasöra geçiş.

# r = os.getcwd() # bulunduğun dosya dizini gösterir.
# print(r)

# os.mkdir("New Directory")   # bulunduğu dizinde yeni bir dosya oluşturur.

# os.makedirs("New Directory/Sub Directory")   # iç içe klasör oluşturmaya yarar

# r = os.listdir()    # Dizindeki ögeleri listeler
# print(r)

# for dosya in os.listdir():      # dizindeki ögeler arasında sonu .py ile biten ögeleri gösterir.
#     if dosya.endswith(".py"):
#         print(dosya)

# import datetime
# r = os.stat("m1.py")    # Dosya hakkında bilgi sahibi olmak istersek
# print(r)    # m1.py ögesi hakkındaki bilgilerin çıktısı
# # r = r.st_size/1024
# r = datetime.datetime.fromtimestamp(r.st_ctime) # m1.py dosyasının oluşturulma tarihinin anlaşılır şekilde çıktısı
# print(r)

# os.system("notepad.exe")    # Windows üzerindeki uygulamaları çalıştırmamızı sağlar. Burada yeni bir notepad çalışır.

# os.rename("New Directory", "Yeni Klasör")   # dizindeki klasörün ismini değiştirir.

# os.rmdir("New Directory")   # klasör silme (alt klasörü olan dosyayı silmez)
# os.removedirs("New Directory/Yeni Klasör") # Alt klasörü olan bir dosyayı komple silme

# r = os.path.abspath("m2.py")    # dosyanın tam yolunu bulur. 
# r = os.path.dirname("C:/Users/ouz/Desktop/BTK Python Eğitimi/15. İleri Seviye Python Modülleri & Web Scraping/m2.py")   # Dosyanın tam yolundan Dizin ismini verir.
# # Yukarıdaki iki çoğu zaman beraber kullanılır:
# r = os.path.dirname(os.path.abspath("m2.py"))   # Yukardaki işlemin tek satırda yapılışı
# print(r)

# r = os.path.exists("m1.py") # Dosyanın olup olmadığını söyler. True/False
# print(r)

# r = os.path.isdir("C:/Users/ouz/Desktop/BTK Python Eğitimi/15. İleri Seviye Python Modülleri & Web Scraping")   # Gösterilern yoldaki öge klasör mü değil mi True/False döndürür.
# print(r)

# r = os.path.isfile("C:/Users/ouz/Desktop/BTK Python Eğitimi/15. İleri Seviye Python Modülleri & Web Scraping")    # Gösterilen yoldaki öge dizin mi değil mi True/false döndürür.
# print(r)

# r = os.path.split("C://deneme")     # dosya yolunu elemanlara böler
# print(r)

# r = os.path.splitext("m1.py")   # Dosya ile uzantısını ayırır.
# print(r)

