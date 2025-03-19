from reader import read 
class Vector :
    def __init__(self, x, y):# конструктор
        self.x = x #перша точка
        self.y = y #друга точка
    def __abs__(self): #метод для обчислення довжини вектора
        return (self.x ** 2.0 + self.y ** 2.0) ** 0.5
    
    
    def plot(self, ax, color='b'): #метод для побудови вектораw
        ax.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=color) #малюємо вектор
        ax.set_xlim(-10, 10) #встановлюємо межі графіку
        ax.set_ylim(-10, 10) #встановлюємо межі графіку
        ax.grid() #вмикаємо сітку

read("input01 (1).txt")
read("input02.txt")
read("input03.txt")


# те що треба зроити в лабі
print(abs)
