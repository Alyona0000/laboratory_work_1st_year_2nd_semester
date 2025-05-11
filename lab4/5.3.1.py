from reader import read 

class Rational:
    
    def __init__(self, a, b=0):
        
        if isinstance (a, Rational):
            self.numerator = a.numerator
            self.denominator = a.denominator
        elif isinstance(a, str) and "/" in a:
            v = a.split("/")
            self.numerator = int(v[0])
            self.denominator = int(v[1])
            print(f"скородити до десятковвого дробу : {self.numerator / self.denominator}")
        elif isinstance(a, str):
            self.numerator = int(a)
            self.denominator = 1
        elif b == 0:
            raise ZeroDivisionError("Ділення на нуль")
        else:
            self.numerator = a
            self.denominator = b
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
        


def Distribution(file_name):
    d=open(file_name) 
    
    for l in d:
            print(l)
            l = l.split()
            m = l[0]
            i = 1
            while  i < len(l): #перетворення рядка у список
                b = l[i]
                q = l[i + 1]
                m = Rational(m)
                q = Rational(q)

                if b == "+":
                    r = m + q
                elif b == "-":
                    r = m - q
                elif b == "*":
                    r = m * q
                elif b== "/":
                    r = m / q
                print(f"{m} {b} {q} = {r}")
                m = r
                i = i + 2

    print("***")
    


Distribution("input01 (1).txt")
