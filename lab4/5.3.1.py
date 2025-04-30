from reader import read 

# раціональне число
class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator # чисельник
        self.denominator = denominator # знаменник
        
    def __str__(self): #перетводення дробу у раціональне число
        return f"{self.numerator}/{self.denominator}"

#ціле число
class Integer:
    def __init__(self, number):
        self.number = number # число
        
    def __str__(self): #перетводення цілого числа у раціональне число
        return f"{self.number}/1"
    
class Arithmetic:
    def __init__(self, add, subtraction, multiplication, division):
        self.add = add
        self.subtraction = subtraction
        self.multiplication = multiplication   множення
        self.division = 



def Distribution(file_name):
    d=open(file_name)
    integer = []
    rational = []
    arithmetic = []
    d = 0
    for namber in (file_name): 
        line = line.split() 
        try:    
            if line[0] == int (namber):
                integer.append(Integer(namber))
            elif line[0] ==  (namber):
            else:
                rational.append(Rational(namber.numerator, namber.denominator))

        except:
            print("Помилка")
            print(line)
            continue
        d = d+1



read("input01 (1).txt")