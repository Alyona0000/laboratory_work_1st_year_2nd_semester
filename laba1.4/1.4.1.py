from reader import read 
class Vector :
    def __init__(self, x, y):# конструктор
        self.x = x #перша точка
        self.y = y #друга точка

    def __add__(self, other): #додавання        __add__ - це оператор + для додавання двох об'єктів.
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other): #віднімання       __sub__ - це оператор - для віднімання одного об'єкта від іншого.
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other): #множення         __mul__ - це оператор * для множення двох об'єктів.
        return Vector(self.x * other.x, self.y * other.y)
    def __truediv__(self, other): #ділення      __truediv__ - це оператор / для ділення одного об'єкта на інший.
        return Vector(self.x / other.x, self.y / other.y)
    def __str__(self): #перетворення в строку   __str__ - це оператор, який повертає рядок, який представляє об'єкт.
        return f'Vector({self.x}, {self.y})'
    def __repr__(self): #перетворення в строку  __repr__ - це оператор, який повертає рядок, який представляє об'єкт.
        return f'Vector({self.x}, {self.y})'
    
    def plot(self, ax, color='b'): #метод для побудови вектораw
        ax.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=color) #малюємо вектор
        ax.set_xlim(-10, 10) #встановлюємо межі графіку
        ax.set_ylim(-10, 10) #встановлюємо межі графіку
        ax.grid() #вмикаємо сітку

read("input01 (1).txt")