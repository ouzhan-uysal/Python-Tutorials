

liste = [1,2,3,4,5]     # liste bir iterable obje. tek tek elemanları arasında dolaşılabilir.
"""
for i in liste:     # elemanlar arasında dolaşma işlemi 
    print(i)
"""
iterator = iter(liste)  # iteratorun oluşturulması

"""
print(next(iterator))   # listenin sırada elemanı gelir
print(next(iterator))
print(next(iterator))
"""

"""
while True:
    try:
        element = next(iterator)
        print(element)

    except StopIteration:
        break
"""

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x

        else:
            raise StopIteration

liste = MyNumbers(20, 50)

for x in liste:
    print(x)