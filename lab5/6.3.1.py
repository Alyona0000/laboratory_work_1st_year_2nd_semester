from RationalList import RationalList

def Distribution(file_name):
    with open(file_name, encoding='utf-8') as d: 
        for line_number, line in enumerate(d, start=1):
            line = line.strip()
            if not line:
                continue  # пропустити порожні рядки

            print(f"Обробка списку з рядка {line_number}: {line}")
            elements = line.split()
            rational_list = RationalList(elements)

            print("Відсортований список:")
            for r in rational_list:
                print(r)

            result = rational_list.sum()
            print(f"Сума чисел в списку: {result}")
            print("---")


Distribution("input03.txt")