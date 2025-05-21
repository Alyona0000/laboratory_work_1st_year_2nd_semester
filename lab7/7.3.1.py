# 7.3.1
# Опишіть клас виключення RationalError, що є нащадком класу ZeroDivisionError та ініціюється у випадку якщо при
# створенні екземпляру класу Rational описаного у задачі 5.3.1. знаменник дорівнює нулю.
class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може дорівнювати нулю"):
        super().__init__(message)
        
class Rational:
    
    def __init__(self, a, b=0):
        
        if isinstance (a, Rational):
            self.numerator = a.numerator
            self.denominator = a.denominator
        elif isinstance(a, str) and "/" in a:
            v = a.split("/")
            self.numerator = int(v[0])
            self.denominator = int(v[1])
        elif isinstance(a, str):
            self.numerator = int(a)
            self.denominator = 1
        elif b == 0:

            raise ZeroDivisionError("Ділення на нуль")
        else:
            self.numerator = a
            self.denominator = b

        a =self.gcd(self.numerator,self.denominator) 
        if a != 1: # скорочення дробу
            self.numerator = self.numerator // a
            self.denominator = self.denominator // a

    def gcd(self, a, b):  # НСД
            while b != 0:
                r = a % b
                a = b
                b = r
            return a
    def __add__(self, y): 
        numerator = self.numerator * y.denominator + y.numerator * self.denominator
        denominator = self.denominator * y.denominator
        return Rational(numerator, denominator) #повертає результат арифметичних ді
    
    def __sub__(self, y):
        numerator = self.numerator * y.denominator - y.numerator * self.denominator
        denominator = self.denominator * y.denominator
        return Rational(numerator, denominator) #повертає результат арифметичних ді

    def __mul__(self, y): 
        numerator = self.numerator * y.numerator
        denominator = self.denominator * y.denominator
        return Rational(numerator, denominator) #повертає результат арифметичних ді

    def __truediv__(self, y) :
        numerator = self.numerator * y.denominator
        denominator = self.denominator * y.numerator
        return Rational(numerator, denominator) #повертає результат арифметичних ді

    def __str__(self): #перетводення дробу у раціональне число
        return f"{self.numerator}/{self.denominator}"
    

    def __getitem__(self, key): # Метод для отримання значення за ключем    
        if key == "n":
            return self.numerator
        elif key == "d":
            return self.denominator
        else:
            raise KeyError("Ключ має бути 'n' або 'd'") 

    def __setitem__(self, key, value): # Метод для встановлення значення за ключем
        if key == "n":  
            self.numerator = value
        elif key == "d":  
            self.denominator = value
        else:
            raise KeyError("Ключ має бути 'n' або 'd'") 
        
    def __call__(self):
        return self.numerator / self.denominator #перетворення дробу у десятковий дріб


def Distribution(file_name):
    with open(file_name) as d: 
        for line in d:
            elements = line.split()
            rationals = []

            for part in elements:
                try:
                    r = Rational(part)
                    rationals.append(r)
                except RationalError as e:
                    print(f"Помилка: {part} — {e}")
                    continue

            if rationals:
                total = rationals[0]
                for r in rationals[1:]:
                    total = total + r
                print(f"Сума чисел в списку: {total}")
            else:
                print("Жодного коректного дробу не знайдено.")
            print("---")

Distribution("input03.txt")