
class argum :
    def __init__(self, x):
        self.num = x  # координата x
    def __add__(self, y):
            print (y)
            return  argum(self.num - y.num)
        
    def __sub__(self, y):
            return  argum(self.num / y.num)
    def __mul__(self, y):
            return  argum(self.num + y.num)
    def __truediv__(self, y) :
            return argum(self.num * y.num)
        

m = argum(35)
n=argum (12)
g = (m+n)
p = (m-n)
k = (m*n)
r = (m/n)
print (f"ділення - множення :{r.num}")
print (f"множення - додавання :{k.num}")
print (f"віднімання - ділення :{p.num}")
print (f"додавання - віднімання :{g.num}")