# Nesned functions  => İç içe fonksiyon kullanımı


# Encapsulation
"""
def outer(num1):
    print("in outer")
    def inner_increment(num1):
        print("in inner")
        return num1 + 1
    
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10)
"""


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number > 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <=1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)

try:
    sayi = input("Faktöriyeli alınacak sayı: ")
    print(factorial(sayi))
except Exception as e:
    print(e)