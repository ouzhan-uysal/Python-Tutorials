
# Reading Files

try: 
    f1 = open("newfile.txt", "r", encoding="utf-8")
    print(f1)
    print("\n")

    # 1. for döngüsü ile okuma
    """
    for i in f1:
        print(i, end="")    # end: satırı okuduktan sonra boş line eklenmesini engeller. Satır sonuna istediğimiz bir şey varsa onu yazabiliriz.
    """

    # 2. Read() fonksiyonu ile okuma
    content1 = f1.read()
    print("-İçerik 1-")
    print(content1)

    print("\n")

    content2 = f1.read()    # Yukarıdaki okuma işleminde dosyadaki tüm satırlar okunur ve kürsör dosyanın en sonuna gelir. Buraya yapılan 2. okumada okuyacak herhangi bir şey olmaz. print dediğimizde hiçbir şey yazılamaz. Eğer tekrar dosya açma işlemi yapılırsa o zaman tekrar çıktı alınır.
    print("-İçerik 2-")
    print(content2)

    print("\n")

    f1 = open("newfile.txt", "r", encoding="utf-8")
    print(f1)
    print("\n")
    content3 = f1.read(7)   # 7 parametresi f1 dosyası içerisindeki ilk 7 karakterin okumasını istenildiğini belirtir.
    content4 = f1.read(6)   # Kürsörün olduğu yerden itibaren okumaya başlar
    print("-İçerik 3-")
    print(content3)
    print(content4)

    print("\n")

    print("-İçerik 4-")
    print(f1.readline())    # Bir sonraki satırı komple yazdırma

    print("\n")

    print("-İçerik 5-")
    print(f1.readlines())   # Kalan tüm satırları dizi elemanları olarak yazar


except FileNotFoundError:
    print("Dosya belirtilen konumda değil.")

finally:
    f1.close()  # finally: Her zaman kodun en sonunda çalışacağı için dosya kapama işlemi burada yapılabilir.
    print("\n\n--- Dosya kapandı ---")