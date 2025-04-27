#str.format(): этот метод позволяет встраивать переменные в строку, используя заполнители {}
a ="        Parallelogram    0    8   21 "
b ="    Triangle   14   16    0 "
c ="    Triangle Parallelogram  14   16    0 "


print(c.split())
f = c.split()
if f[0] == "Parallelogram" :
         print("Паралелограм")

##def split_string(input_string):
    # Используем регулярное выражение для разделения строки на слова и числа
  #  parts = re.findall(r'\b\w+\b', input_string) # \b - граница слова, \w+ - одно или более буквенно-цифровых символов
   # words = [part for part in parts if part.isalpha()] # Проверяем, является ли часть слова
    #numbers = [part for part in parts if part.isdigit()] # Проверяем, является ли часть числом
    #return words, numbers

#input_string = "        Parallelogram    0    8   21 "
#words, numbers = split_string(input_string)

#print("Слова:", words)
#print("Числа:", numbers)





