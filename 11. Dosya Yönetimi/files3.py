
with open("newfile.txt", "r", encoding="utf-8") as f1:     # with:dosya kapamayı kendisi otomatik yapar bizim yapmamıza gerek kalmaz. f1: referans
    content = f1.read(10)
    print(content)
    print("Kürsörün Konumu: ", f1.tell())    # kürsörün konumu verir
    f1.seek(0)  # Kürsörün konumunu değiştirir.
    print("Kürsörün Şuanki Konumu: ", f1.tell())
    content2 = f1.read(20)
    print(content2)
    f1.seek(5)
    print("Kürsörün Şuanki Konumu: ", f1.tell())

# Dosyayı Güncelleme

with open("newfile.txt", "r+", encoding="utf-8") as f2:     # r+ ile klasörün başından ekleme yapılır.
    print("Kürsörün Şuanki Konumu: ", f2.tell())

with open("newfile.txt", "a", encoding="utf-8") as f3:      # a ile klasörün sonuna ekleme yapılır.
    print("Kürsörün Şuanki Konumu: ", f3.tell())