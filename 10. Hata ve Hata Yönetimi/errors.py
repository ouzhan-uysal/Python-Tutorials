# Errors:
"""
NameError   => Tanımlanmamış bir veri kullanıldığında alınan hata. Örn: print(a)
ValueError  => Int olmayan değeri int  yapmaya çalışırsan alacağın error. Örn: int('1a2')
ZeroDivisionError   => Sıfıra bölme hatası.
SyntaxError => Yanlış bir ifade yani yazım yanlışı olduğunda karşılaşılan hata. Örn: print("denem"e)
"""

# Error Handling => Hata Yönetimi
"""
Hata gelebilecek kod blokları try içine alınır. Öngörülen hata türüde except kısmına yazılır.
"""

while True:
    try: 
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)

    except ZeroDivisionError:
        print("y nin değeri 0 olamaz.")

    except ValueError:
        print("Her iki değişkeninde değeri Int olmalıdır.")
    # or
    except (ZeroDivisionError, ValueError) as e:    # yukardaki 2 except yerine alttaki tek except yazılabilir.
        print("Girdiğiniz değerler yanlış veya y değeri 0")
        print("Alınan Hata: ", e)
    # or
    except Exception as e:  # Tüm hataları kapsar.
        print(e)

    else:   # Hata olduğu sürece buraya giremeyecek ve döngü sürekli devam edecek.
        print("Herhangi bir hata alınmadı. Her şey yolunda.")
        break

    finally:    # Yukarıda ne olursa olsun sonunda çalışacak olan kısım.
        print("Hamdolsun çalışıyoruz.")
        # Burada genelde yapılan işlemi sonlandırmak amacıyla kullanılıyor. Mesela yukarıda bi .txt dosyası açıldıysa burada kapatılabiliyor.