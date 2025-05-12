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
    





f = RationalList(["4/3", "2/5", "1/2"])
print(f"кількість елементів у списку: {len(f)}")
############################################################## 


# iadd
f += "3/7"
  # 4/3, 2/5, 1/2, 3/7
print(f"кількість елементів у списку: {len(f)}")

g = RationalList(["1/1"])
f += g
 # 4/3, 2/5, 1/2, 3/7, 1/1
print(f"кількість елементів у списку: {len(f)}")


f += 10
 # 4/3, 2/5, 1/2, 3/7, 1/1
print(f"кількість елементів у списку: {len(f)}")


############################################################## 
r1 = RationalList(["1/2", "2/3"])
r2 = RationalList(["4/5"])

r3 = r1 + r2         # Два списки
r4 = r1 + 3          # Додати int
r5 = r1 + Rational(5, 2)  # Додати Rational

print(r1[1])

print(r3[2])



def Distribution(file_name):
    d=open(file_name) 
    
    for l in d:
            print(l)
            l = l.split()