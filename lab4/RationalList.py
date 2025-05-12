from Rational import Rational 

class RationalList:
    def __init__(self, args):
        self.rationals = [Rational(arg) for arg in args] # заміна цикло


    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList(self.rationals + other.rationals)
        elif isinstance(other, Rational):
            return RationalList(self.rationals + [other])
        elif isinstance(other, int):
            return RationalList(self.rationals + [Rational(other, 1)])
        else:
            raise TypeError("Правий операнд має бути RationalList, Rational або int")
        
    def __getitem__(self, index): # Метод для отримання значення за індексом
        return self.rationals[index]

    def __setitem__(self, index, value): # Метод для встановлення значення за індексом
        if isinstance(value, Rational):
            self.rationals[index] = value
        elif isinstance(value, int):
            self.rationals[index] = Rational(value, 1)
        elif isinstance(value, str):
            self.rationals[index] = Rational(value)
        else:
            raise TypeError("Можна встановлювати тільки Rational, int або str")
        
    def __call__(self, index): # Метод для отримання значення за індексом
         return self.rationals[index]
    
    
    def __len__(self):
     return len(self.rationals)
    

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.rationals += other.rationals
        else:
            self.rationals.append(Rational(other,1))
        return self
    def sum(self):
        total = Rational(0,1) # Початкова сума
        for rational in self.rationals:
            total += rational
        return total


def Distribution(file_name):
    with open(file_name) as d: 
        for line in d:

            #print(f"Обробка списка: {line.strip()}")
            elements = line.split()
            rational_list = RationalList(elements)  

            result = rational_list.sum()  
            print(f"Сума чисел в списку: {result}")
        print("---")

Distribution("input03.txt")