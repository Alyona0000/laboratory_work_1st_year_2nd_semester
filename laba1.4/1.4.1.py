from reader import read 
class Vector :
    def __init__(self, x,y):# конструктор
        self.x = x #перша точка
        self.y = y #друга точка
   
    
    def plot(self, ax, color='b'): #метод для побудови вектораw
        ax.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=color) #малюємо вектор
        ax.set_xlim(-10, 10) #встановлюємо межі графіку
        ax.set_ylim(-10, 10) #встановлюємо межі графіку
        ax.grid() #вмикаємо сітку
# розмырнысть вектора з файлу
   # def __len__(self):
 #3.2 - визначити розмірність вектора. викликати метод get_size створеного у пункті 3.1 обєкту
  #     file.read
        
class Vector2 :
    def __init__(self, arg):# конструктор
        if isinstance(arg, Vector2): # a є екземпляром Triangle
            self.coordz = arg.coordz
        else:
            self.coordz = arg
    def print (self):
        print(self.coordz)    
    
    def get_size(self):
        return len(self.coordz)
    def __abs__(self): #метод для обчислення довжини вектора
        return (self.x ** 2.0 + self.y ** 2.0) ** 0.5
    
#read("input02.txt")
#read("input03.txt")

def main ():
    i=0
    lines = read("input01 (1).txt")
    while i < len(lines):
        line = lines[i].split()
        v= Vector2(line)
        v.print()
        print(v.get_size())
        i += 1

#3.1 - створити об'ект вектор із масиву елементів одніеї строки 
#3.3 - вивести на екран розмірність    

# те що треба зроити в лабі
main()

