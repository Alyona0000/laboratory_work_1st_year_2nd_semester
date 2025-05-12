u=[
"1",
"+", "2",
"-", "3",
"-", "4",
"*","78"
]
class Ccc:
    def __init__(self, oper):
        self.q = int(oper[0])
        i = 1
        while i < len(oper):
            op = oper[i]
            b = int(oper[i + 1])
            if op == "+":
                self.q = self.q + b
            elif op == "-":
                self.q = self.q - b
            elif op == "*":
                self.q = self.q * b
            elif op == "/":
                self.q = self.q / b
            i = i + 2

    def result(self):
        return self.q

class EEe :
    def __init__(self, x):
        self.x = x  # координата x
    def __add__(self):
            return  EEe(self.x - self.x)
        
    def __sub__(self):
            return  EEe(self.x / self.x)
        

m = EEe(35)
print(m.__add__())
print(m.__sub__())

a = int(u[0])
i = 1

while i < len(u):
    m = u[i]
    b = int(u[i + 1])
    if m == "+":
        a = a + b
    elif m == "-":
        a = a - b
    elif m == "*":
        a = a * b
    elif m == "/":
        a = a / b

    i = i + 2

#print(a)



