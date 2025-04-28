#1.3.1. Опишіть класи для таких геометричних фігур зазначених нижче: 
#• Трикутник – визначається довжинами трьох сторін.
#• Прямокутник – визначається двома сторонами
#• Трапеція – визначається двома основами та двома бічними сторонами.
#• Паралелограм – визначається двома сторонами та висотою.
#• Круг – визначається радіусом.
#У кожному з класів реалізуйте операції знаходження периметра (для кола 
#– довжини кола) та площі. За допомогою цих класів розв’яжіть таку задачу: 
#Задано список фігур вищенаведених класів. Серед заданих фігур знайдіть 
#фігуру, що має найбільшу площу та периметр.
#Перелік фігур зберігається у текстовому файлі – у кожному окремому рядку 
#файла вказується назва фігури та список параметрів, що визначають фігуру 
#відповідно до зазначеного вище. Параметри розділені одним або кількома 
#символами пропуску. Назви фігур вказані таким чином: Triangle – Трикутник, 
#Rectangle – Прямокутник, Trapeze – Трапеція, Parallelogram – Паралелограм, 
#Circle – Круг.                            
#Вхідні дані містяться файлах
#input01.txt
#input02.txt
#input03.txt
#за посиланням


from reader import read 
import math
import os # Імпортуємо модуль os для роботи з операційною системою

class Triangle:
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



class Rectangle:
    def __init__(self, width, height):  # Ініціалізація об'єкта класу Rectangle
        self.width = width  # Збереження ширини прямокутника
        self.height = height  # Збереження висоти прямокутника


        if not self.is_valid():
         raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
        return self.width > 0 and self.height > 0

    def perimeter(self):  # Метод для обчислення периметра
        return 2 * (self.width + self.height) # Периметр прямокутника
    def area(self):  # Метод для обчислення площі
        return self.width * self.height # Площа прямокутника

class Parallelogram:
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
    def area(self):  # Метод для обчислення площі паралелограма
        return self.base * self.height # Площа паралелограма
        

class Circle:
    def __init__(self, radius):  # Ініціалізація об'єкта класу Circle
        self.radius = radius  # радіуса кола

        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує") # Перевірка чи існує трикутник з такими сторонами
    
    def is_valid(self):
       return self.radius > 0
    
    def perimeter(self):  # Метод для обчислення довжини кола
        return 2 * math.pi * self.radius # Довжина кола
    def area(self):  # Метод для обчислення площі паралелограма
        return math.pi * self.radius ** 2 # Площа кола    
    
def Distribution(file_name):
    d=open(file_name) # Викликаємо функцію read для зчитування файлу
    max_area =0
    max_perimeter = 0 # Ініціалізуємо максимальний периметр
    max_area_obj = None # Ініціалізуємо максимальну площу та об'єкт з максимальною площею
    max_perimeter_obj = None # Ініціалізуємо максимальний периметр та об'єкт з максимальною площею
    for line in d: 
        line = line.split()  
        try:
            if line[0] == "Parallelogram" :
                obj = Parallelogram(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Parallelogram
            elif line[0] == "Circle" :
                obj = Circle(float(line[1])) # Створюємо об'єкт класу Circle
            elif line[0] == "Rectangle" :
                obj = Rectangle(float(line[1]), float(line[2])) # Створюємо об'єкт класу Rectangle
            elif line[0] == "Triangle" :
                obj = Triangle(float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Triangle
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
        if obj.perimeter() > max_perimeter: # Якщо периметр фігури більший за максимальну площу
            max_perimeter = obj.perimeter() # Оновлюємо максимальну площу
            max_perimeter_obj = obj # Оновлюємо об'єкт з максимальною площею

    print("=======================")
    print(f"Максимальна площа: {max_area_obj.area()}") # Виводимо максимальну площу
    print(max_area_obj)

    print(f"Максимальний периметр : {max_area_obj.perimeter()}") # Виводимо максимальний периметр            
    print (max_perimeter_obj)
  

read("input01.txt")
read("input02.txt")
read("input03.txt")

# Основна програма
content_file = input("Введіть ім'я файлу зі списком файлів: ") # Запитуємо ім'я файлу зі списком файлів
Distribution(content_file) # Викликаємо функцію Distribution для розподілу фігур по файлах
#result = sum_numbers_from_files(content_file) # Підсумовуємо числа з файлів

