from reader import read 
#клас список
class RationalList:
    def __init__(self):
         self.rational_list = [] # Ініціалізуємо порожній список для зберігання раціональних чисел
        
    def add(self, number): # Метод для додавання раціонального числа до списку
        if isinstance(number, Rational): # Перевіряємо, чи є number об'єктом класу Rational
            self.rational_list.append(number)
        else: # Якщо number не є об'єктом класу Rational, виводимо повідомлення про помилку
            print("Помилка: потрібно передати об'єкт класу Rational")
    def __str__(self): # Метод для виведення списку раціональних чисел у вигляді рядка
        return str(self.rational_list) # Повертаємо рядкове представлення списку раціональних чисел
#клас раціональне число
class Rational:
    def __init__(self, numerator, denominator): # Ініціалізуємо чисельник та знаменник
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self): # Метод для виведення раціонального числа у вигляді рядка
        return f"{self.numerator}/{self.denominator}" # Повертаємо рядкове представлення раціонального числа








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
                obj = (float(line[1]), float(line[2]), float(line[3])) # Створюємо об'єкт класу Parallelogram
            elif line[0] == "Circle" :
                obj = (float(line[1])) # Створюємо об'єкт класу Circle

        except:
                print("Помилка при створенні фігури")
                print(line)
                continue
    

read("input01.txt")
read("input02.txt")
read("input03.txt")
