# Re Modülü

import re   # Regular Expressions   => Arama ile sonuç döndürür.

# r = dir(re)
# print(r)

str = "Oğuzhan Uysal | Computer Eng"

# r = re.findall("Oğuzhan", str)  # str içinde belirtilen string'ten kaç tane olduğunu gösterir. len(r) yaparsan kaçtane olduğunun sayısını alırsın.
# print(r)

# r = re.split(" ", str)  # str içerisindeki yazıyı " " lara göre elemanlara böler.
# print(r)

# r = re.sub("\s", "-", str)   # str içerisindeki boşlukları - ile değiştirir.
# print(r)

# r = re.search("Com", str)   #  str içerisinde Com ifadesiyle karşılaştığı ilk indexleri döndürür.
# print(r)
# r = r.span()   # yukarıdaki konumu direk verir
# print(r)
# Asıl kullanımı:
# r = re.search("Com", str).span()
# print(r)
# r = r.start()   # başlangıç indeksi
# print(r)
# r = r.end()     # bitiş indeksi
# print(r)

# Karakter Arama:
# r = re.findall("[abc]", str)    # bulduğu tüm a, b ve c karakterlerinin çıktısını verir.
# print(r)

# r = re.findall("[saat]", str)   # s, a, t karakterlerini arar. "saat" olarak değil.
# print(r)

# r = re.findall("[d-k]", str)    # d'den k'ye kadar olan tüm karakterleri arar. [1-5] yaparsan 1'den 5'e kadar olan rakamları arar.
# print(r)

# r = re.findall("...", str)
# print(r)

# r = re.findall("U...l", str)    # Uysal ifadesi gelir.
# print(r)

"""
a,b,c karakterleri dışındaki diğer karakterleri aramak istiyorsan [^abc] şeklinde arama yapılır.
Eğer arama yerine "." konursa tüm karakterleri tek tek verir. "..." şeklinde arama yapılırsa karakterleri 3er basamaklı olarak yazdırır.
"^"   => belirtilen karakterle başlıyor mu?
    ^a  => dersek a ile başlayan kelime olup olmadığı söyler
"$" => belirtilen karakterle bitiyor mu?
    $a  => dersek a ile biten kelime olup olmadığını söyler


"""

