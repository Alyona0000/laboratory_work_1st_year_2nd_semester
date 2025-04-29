from reader import read 
import math

class Triangle: #Трикутник================================================
    def __init__(self, a, b, c):
        self.a = a # Ініціалізація об'єкта класу Triangle сторона трикутника
        self.b = b
        self.c = c
        
        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами
    def perimeter(self):  # Метод для обчислення периметра
        return self.a + self.b + self.c     # Периметр трикутника
       
    
    def area(self):  # Метод для обчислення площі трикутника
        s = self.perimeter() / 2
        a = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # Площа трикутника
        return a



class TriangularPyramid: #Трикутна піраміда================================================
    def __init__(self, a, b, c, height):  # Ініціалізація об'єкта класу TriangularPyramid
        self.a = a  # Сторона трикутника
        self.b = b  # Сторона трикутника
        self.c = c  # Сторона трикутника
        self.height = height  # Висота піраміди

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами

    def area(self):  # Метод для обчислення площі піраміди
        s = (self.a + self.b + self.c) / 2
        area_triangle = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Площа основи піраміди
        return area_triangle * self.height / 3  # Площа піраміди


class QuadrangularPyramid: #Чотирикутна піраміда================================================
    def __init__(self, a, b, c, d, height):  # Ініціалізація об'єкта класу QuadrangularPyramid
        self.a = a  # Сторона трикутника
        self.b = b  # Сторона трикутника
        self.c = c  # Сторона трикутника
        self.d = d  # Сторона трикутника
        self.height = height  # Висота піраміди

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами

    def area(self):  # Метод для обчислення площі піраміди
        s = (self.a + self.b + self.c + self.d) / 2
        area_triangle = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d))  # Площа основи піраміди
        return area_triangle * self.height / 3  # Площа піраміди


class Rectangle: #Прямокутник================================================
    def __init__(self, width, height):  # Ініціалізація об'єкта класу Rectangle
        self.width = width  # Збереження ширини прямокутника
        self.height = height  # Збереження висоти прямокутника


        if not self.is_valid():
         raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.width > 0 and self.height > 0
    
    def area(self):  # Метод для обчислення площі
        return self.width * self.height # Площа прямокутника

class Parallelogram: #Паралелограм================================================
    def __init__(self, base, side, height):
        self.base = base # база(нижня сторона) паралелограма
        self.side = side # сторона паралелограма
        self.height = height # висота паралелограма


        if not self.is_valid():
             raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        self.base > 0
        self.side > 0
        self.height > 0
        return
    
    def area(self):  # Метод для обчислення площі паралелограма
        return self.base * self.height # Площа паралелограма
        
class Trapeze: #Трапеція================================================
    def __init__(self, base1, base2, height):  # Ініціалізація об'єкта класу Trapeze
        self.base1 = base1  # Збереження основи трапеції
        self.base2 = base2  # Збереження основи трапеції
        self.height = height  # Збереження висоти трапеції

        if not self.is_valid():
            raise ValueError("Трапеція із такими сторонами не існує") # Перевірка чи існує трапеція з такими сторонами
    
    def is_valid(self):
        return self.base1 > 0 and self.base2 > 0 and self.height > 0
    
    def area(self):  # Метод для обчислення площі трапеції
        return (self.base1 + self.base2) * self.height / 2 # Площа трапеції


class Circle: #Коло================================================
    def __init__(self, radius):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола

        if not self.is_valid():
            raise ValueError("--- Таке коло не існує") # Перевірка чи існує коло з таким радіусом
    
    def is_valid(self):
       return self.radius > 0
    
    def area(self):  # Метод для обчислення площі паралелограма
        return math.pi * self.radius ** 2 # Площа кола    
    

class Ball : #Куля================================================
    def __init__(self, radius):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола
        
        if not self.is_valid():
            raise ValueError("Таке коло не існує") # Перевірка
    
    def is_valid(self):
       return self.radius > 0
    
    def area(self):  # Метод для обчислення площі паралелограма
        return 4 * math.pi * self.radius ** 2 # Площа кола    
    
class Cone: #Конус================================================
    def __init__(self, radius, height):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола
        self.height = height  # висота конуса

        if not self.is_valid():
            raise ValueError("Таке коло не існує")
        

    def slant_height(self): # Похила висота конуса
        return math.sqrt(self.radius**2 + self.height**2)

    def surface_area(self): # Площа поверхні конуса
        l = self.slant_height()
        return math.pi * self.radius * (self.radius + l)

    def volume(self): # Обʼєм конуса
        return (1/3) * math.pi * self.radius**2 * self.height
    
def Distribution(file_name):
    d=open(file_name) # Викликаємо функцію read для зчитування файлу
    max_area =0
    max_area_obj = None # Ініціалізуємо максимальну площу та об'єкт з максимальною площею
    for line in d: 
        line = line.split()  
        try:
            if line[0] == "Triangle" :
                obj = Triangle(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Triangle
            elif line[0] == "TriangularPyramid" :
                obj = TriangularPyramid(float(line[1])) # Створюємо об'єкт класу TriangularPyramid
            elif line[0] == "QuadrangularPyramid" :
                obj = QuadrangularPyramid(float(line[1]), float(line[2])) # Створюємо об'єкт класу QuadrangularPyramid
            elif line[0] == "Rectangle" :
                obj = Rectangle(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Rectangle
            elif line[0] == "Parallelogram" :
                obj = Parallelogram(float(line[1])) # Створюємо об'єкт класу Parallelogram
            elif line[0] == "Trapeze" :
                obj = Trapeze(float(line[1]), float(line[2])) # Створюємо об'єкт класу Trapeze
            elif line[0] == "Circle" :
                obj = Circle(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Circle
            elif line[0] == "Ball" :
                obj = Ball(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Ball
            elif line[0] == "Cone" :
                obj = Cone(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Cone
            else:
                print("Невідомий тип фігури")
                continue  # Пропускаємо невідомі фігури
        except:
            print("Помилка при створенні фігури")
            print(line)
            continue


        print(f"{line[0]} area:{obj.area()}") # Виводимо площу фігури
        if obj.area() > max_area: # Якщо площа фігури більша за максимальну площу
            max_area = obj.area() # Оновлюємо максимальну площу
            max_area_obj = obj # Оновлюємо об'єкт з максимальною площею   

    print("=======================")
    print(f"Максимальна площа: {max_area_obj.area()}") # Виводимо максимальну площу
    print(max_area_obj)
    print("=======================")

read("input01.txt")
read("input02.txt")
read("input03.txt")


# Основна програма
content_file = input("Введіть ім'я файлу зі списком файлів: ") # Запитуємо ім'я файлу зі списком файлів
Distribution(content_file) # Викликаємо функцію Distribution для розподілу фігур по файлах





