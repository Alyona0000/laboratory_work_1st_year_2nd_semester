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

            
    def __str__(self): #перетводення дробу у раціональне число
        return f"{self.numerator}/{self.denominator}"

f = Rational("48")
print(f.numerator)
print(f.denominator)




