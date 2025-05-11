from Rational import Rational 

class RationalList:
    def __init__(self, args):
        self.rationals = [Rational(arg) for arg in args] # заміна цикло


    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList(self.rationals + other.rationals)
        else:
            return RationalList(self.rationals + [Rational(other)])


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
        return self.numerator / self.denominator
    
    
    def __len__(self):
     return len(self.rationals)

    

f = RationalList(["4/3", "2/5", "1/2"])
print(f)
print(len(f))