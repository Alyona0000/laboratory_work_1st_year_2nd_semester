import math
import os

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        if not self.is_valid():
            raise ValueError("Трикутник із такими сторонами не існує")
    
    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height
    
    def perimeter(self):
        return 2 * (self.base + self.side)
    
    def area(self):
        return self.base * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self.radius})"


def read_numbers_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"Файл {file_name} порожній.")
                return None
            shape_type = lines[0].strip()
            numbers = [float(x) for line in lines[1:] for x in line.split()]
            
            if shape_type == 'Parallelogram' and len(numbers) == 3:
                print("паралелограм(*_*")
                return Parallelogram(*numbers)
            elif shape_type == 'Triangle' and len(numbers) == 3:
                print("трикутник(*_*")
                return Triangle(*numbers)
            elif shape_type == 'Circle' and len(numbers) == 1:
                print("коло(*_*")
                return Circle(*numbers)
                
            else:
                print("Невідомий тип фігури або неправильна кількість параметрів")
                return None
    except (FileNotFoundError, PermissionError):
        print(f"Не вдалося відкрити файл: {file_name}")
        return None
    except ValueError:
        print(f"У файлі {file_name} є недійсні числа.")
        return None


def sum_numbers_from_files(content_file):
    if not os.path.exists(content_file):
        print(f"Файл {content_file} не знайдено!")
        return 0.0

    total_sum = 0.0
    try:
        with open(content_file, 'r') as file:
            for file_name in file:
                file_name = file_name.strip()
                print(f"Зчитано файл: {file_name}")
                shape = read_numbers_from_file(file_name)
                if shape:
                    total_sum += shape.area()
    except (FileNotFoundError, PermissionError):
        print(f"Не вдалося відкрити файл: {content_file}")
    
    return total_sum


# Основна програма
content_file = input("Введіть ім'я файлу зі списком файлів: ")
result = sum_numbers_from_files(content_file)
print(f"Загальна сума площ фігур з файлів: {result}")
