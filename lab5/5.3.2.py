from RationalList import RationalList

def Distribution(file_name):
    with open(file_name) as d: 
        for line in d:

            #print(f"Обробка списка: {line.strip()}")
            elements = line.split()
            rational_list = RationalList(elements)  

            result = rational_list.sum()  
            print(f"Сума чисел в списку: {result}")
        print("---")

Distribution("input03.txt")