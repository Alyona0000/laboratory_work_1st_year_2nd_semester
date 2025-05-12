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
            
    def __str__(self): #перетводення дробу у раціональне число
        return f"{self.numerator}/{self.denominator}"

f = Rational("4/3")
print(f.numerator)
print(f.denominator)




