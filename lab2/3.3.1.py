from reader import read 
import math


class Figure: #Базовий клас для всіх фігур================================================
    def __init__(self):
        pass  # Базовий клас не має атрибутів

    def dimension(self):  
        raise NotImplementedError("Цей метод потрібно реалізувати в підкласах")  

    def square(self): 
        raise NotImplementedError("Цей метод потрібно реалізувати в підкласах")  

    def perimeter(self):
        raise NotImplementedError("Цей метод потрібно реалізувати в підкласах")  

    def  squareSurface(self):
          raise NotImplementedError("Цей метод потрібно реалізувати в підкласах") 

    def  squareBase(self):
          raise NotImplementedError("Цей метод потрібно реалізувати в підкласах") 

    def   height(self):
          raise NotImplementedError("Цей метод потрібно реалізувати в підкласах") 

    def   volume(self):
          raise NotImplementedError("Цей метод потрібно реалізувати в підкласах") 




class Triangle(Figure): #Трикутник================================================
    def __init__(self, a, b, c):
        self.a = a # Ініціалізація об'єкта класу Triangle сторона трикутника
        self.b = b
        self.c = c
        self.dimension = 2 # Вимірювання трикутника
        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами
    
    def perimeter(self):  # Метод для обчислення периметра
        return self.a + self.b + self.c     # Периметр трикутника

    def square(self):  # Метод для обчислення площі трикутника
        s = self.perimeter() / 2
        a = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # Площа трикутника
        return a
    
    def dimension(self): 
        return self.dimension
class TriangularPrism(Triangle): #Трикутна піраміда================================================
    def __init__(self, a, b, c, height):  # Ініціалізація об'єкта класу TriangularPyramid
        self.a = a  # Сторона трикутника
        self.b = b  # Сторона трикутника
        self.c = c  # Сторона трикутника
        self.height = height  # Висота піраміди
        self.dimension = 3 # Вимірювання піраміди
        
        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами

    def perimeter(self):  # Метод для обчислення периметра
        return self.a + self.b + self.c

    def square(self):  
            s = (self.a + self.b + self.c) / 2
            square_triangle = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return square_triangle * self.height
    def dimension(self): 
        return self.dimension

class TriangularPyramid(Triangle): #Трикутна піраміда================================================
    def __init__(self, a, b, c, height):  # Ініціалізація об'єкта класу TriangularPyramid
        self.a = a  # Сторона трикутника
        self.b = b  # Сторона трикутника
        self.c = c  # Сторона трикутника
        self.height = height  # Висота піраміди
        self.dimension = 3 # Вимірювання піраміди

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a   # Перевірка чи існує трикутник з такими сторонами

    def perimeter(self):  # Метод для обчислення периметра
        return self.a + self.b + self.c

    def square(self):  # Метод для обчислення площі піраміди
        s = (self.a + self.b + self.c) / 2
        square_triangle = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Площа основи піраміди
        return square_triangle * self.height / 3  # Площа піраміди

    def dimension(self): 
        return self.dimension

class Quadrilateral(Figure): #Чотирикутник================================================
    def __init__(self, a, b):
        self.a = a  # Ініціалізація об'єкта класу Quadrilateral
        self.b = b  # Сторона трикутника
        self.diagonal = 2 # Вимірювання чотирикутника

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    def is_valid(self):
        return self.a > 0 and self.b > 0 # Перевірка чи існує трикутник з такими сторонами




class QuadrangularPyramid(Quadrilateral): #Чотирикутна піраміда================================================
    def __init__(self, a, b, height):  # Ініціалізація об'єкта класу QuadrangularPyramid
        self.a = a  # Сторона трикутника
        self.b = b  # Сторона трикутника
        self.height = height  # Висота піраміди

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.a > 0 and self.b > 0 and self.height > 0
    def perimeter(self):  # Метод для обчислення периметра
        return 2 * (self.a + self.b)

    def square(self):  # Метод для обчислення площі піраміди
        return self.a * self.b + 2 * (self.a + self.b) * math.sqrt(self.height**2 + ((self.a - self.b) / 2)**2)


class Rectangle(Quadrilateral): #Прямокутник================================================
    def __init__(self, width, height):  # Ініціалізація об'єкта класу Rectangle
        self.width = width  # Збереження ширини прямокутника
        self.height = height  # Збереження висоти прямокутника


        if not self.is_valid():
         raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.width > 0 and self.height > 0
    def perimeter(self):  # Метод для обчислення периметра
        return 2 * (self.width + self.height) # Периметр прямокутника

    def square(self):  # Метод для обчислення площі
        return self.width * self.height # Площа прямокутника

class Parallelogram(Quadrilateral): #Паралелограм================================================
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
    

    
    def perimeter(self):  # Метод для обчислення периметра
        return 2 * (self.base + self.side) # Периметр паралелограма
    def square(self):  # Метод для обчислення площі паралелограма
        return self.base * self.height # Площа паралелограма
        
class Trapeze(Quadrilateral): #Трапеція================================================
    def __init__(self, base1, base2, height):  # Ініціалізація об'єкта класу Trapeze
        self.base1 = base1  # Збереження основи трапеції
        self.base2 = base2  # Збереження основи трапеції
        self.height = height  # Збереження висоти трапеції

        if not self.is_valid():
            raise ValueError("Трапеція із такими сторонами не існує") # Перевірка чи існує трапеція з такими сторонами
    
    def is_valid(self):
        return self.base1 > 0 and self.base2 > 0 and self.height > 0
    def perimeter(self):  # Метод для обчислення периметра
        return self.base1 + self.base2 + 2 * math.sqrt(self.height**2 + ((self.base1 - self.base2) / 2)**2)

    def square(self):  # Метод для обчислення площі трапеції
        return (self.base1 + self.base2) * self.height / 2 # Площа трапеції


class Circle(Figure): #Коло================================================
    def __init__(self, radius):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола

        if not self.is_valid():
            raise ValueError("--- Таке коло не існує") # Перевірка чи існує коло з таким радіусом
    
    def is_valid(self):
       return self.radius > 0
    
    def square(self):  # Метод для обчислення площі паралелограма
        return math.pi * self.radius ** 2 # Площа кола    
    def perimeter(self):  # Метод для обчислення довжини кола
        return 2 * math.pi * self.radius # Довжина кола
    

class Ball(Circle): #Куля================================================
    def __init__(self, radius):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола
        
        if not self.is_valid():
            raise ValueError("Таке коло не існує") # Перевірка
    
    def is_valid(self):
       return self.radius > 0
     
    def perimeter(self):  # Метод для обчислення довжини кола
        return 2 * math.pi * self.radius # Довжина кола
    
    def square(self):  # Метод для обчислення площі паралелограма
        return 4 * math.pi * self.radius ** 2 # Площа кола    
    
class Cone(Circle): #Конус================================================
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
    max_square =0
    max_perimeter = 0 # Ініціалізуємо максимальний периметр
    max_square_obj = None # Ініціалізуємо максимальну площу та об'єкт з максимальною площею
    max_perimeter_obj = None # Ініціалізуємо максимальний периметр та об'єкт з максимальною площею
    for line in d: 
        line = line.split()  
        try:
            if line[0] == "Triangle" :
                obj = Triangle(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Triangle
            elif line[0] == "TriangularPyramid" :
                obj = TriangularPyramid(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу TriangularPyramid
            elif line[0] == "QuadrangularPyramid" :
                obj = QuadrangularPyramid(float(line[1]), float(line[2]),  float(line[3])) # Створюємо об'єкт класу QuadrangularPyramid
            elif line[0] == "Rectangle" :
                obj = Rectangle(float(line[1]), float(line[2])) # Створюємо об'єкт класу Rectangle
            elif line[0] == "Parallelogram" :
                obj = Parallelogram(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Parallelogram
            elif line[0] == "Trapeze" :
                obj = Trapeze(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Trapeze
            elif line[0] == "Circle" :
                obj = Circle(float(line[1])) # Створюємо об'єкт класу Circle
            elif line[0] == "Ball" :
                obj = Ball(float(line[1])) # Створюємо об'єкт класу Ball
            elif line[0] == "Cone" :
                obj = Cone(float(line[1]), float(line[2]))
            elif line[0] == "TriangularPrism" :
                obj = TriangularPrism(float(line[1]), float(line[2]), float(line[3]),  float(line[4]))

            else:
                print(f"Невідомий тип фігури - {line[0]}") # Якщо фігура невідома, виводимо повідомлення
                continue  # Пропускаємо невідомі фігури
        except:
            print("Помилка при створенні фігури:") # Якщо сталася помилка при створенні фігури, виводимо повідомлення
            print(line)
            continue


        print(f"{line[0]} area:{obj.square()}") # Виводимо площу фігури
        if obj.square() > max_square: # Якщо площа фігури більша за максимальну площу
            max_square = obj.square() # Оновлюємо максимальну площу
            max_square_obj = obj # Оновлюємо об'єкт з максимальною площею   
        if obj.perimeter() > max_perimeter: # Якщо периметр фігури більший за максимальну площу
            max_perimeter = obj.perimeter() # Оновлюємо максимальну площу
            max_perimeter_obj = obj # Оновлюємо об'єкт з максимальною площею

    print("=======================")
    print(f"Максимальна площа: {max_square_obj.square()}") # Виводимо максимальну площу
    print(max_square_obj)
    print(f"Максимальний периметр : {max_square_obj.perimeter()}") # Виводимо максимальний периметр            
    print (max_perimeter_obj)
    print("=======================")

# Основна програма
#content_file = input("Введіть ім'я файлу (0^0) : ") # Запитуємо ім'я файлу зі списком файлів
content_file = "input03.txt"
Distribution(content_file) # Викликаємо функцію Distribution для розподілу фігур по файлах





