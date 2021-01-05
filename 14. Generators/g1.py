"""
def cube():
    for i in range(5):
        yield i ** 3    # yield ile saklanmayan bir değer tutuluyor. Yani burada oluşan veriye sonradan ulaşılamaz çünkü bellekte tutulmayacak. Değer anlık üretilip anlık kullanılır.

for i in cube():      # Stopiterator hatası almadan dolaşmayıda sağlıyor.
    print(i)
"""

# liste = [i**3 for i in range(5)]    # köşeli parantezde liste gelir.
# print(liste)

generator = (i**3 for i in range(5))    # normal parantezde generator objesi gelir.
for i in generator:
    print(i)