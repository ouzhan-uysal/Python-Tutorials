
class Person:
    def __init__(self, name, year):
        if len(name)> 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:   # geçerli bir name bilgisi gelirse name set edilecek.
            self.name = name

p = Person("Oğuzhan", 1996)