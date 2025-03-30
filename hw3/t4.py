import random
y = 0
float_list = [] # список дробных значений элементов списка
elements = []  # основной список
numbers_count = int(input('Ведите количество элементов списка \n'))
for x in range(numbers_count):
    elements.append(round(random.uniform(0, 10),2))
print(elements)
for x in elements:
    float_list.append((x) - int((x)))
#   print(abs(x) - int(abs(x)))
min_fractional = round(min(float_list), 2)  # минимальная дробная часть
max_fractional = round(max(float_list), 2)  # максимальная дробная часть
print(f'Минимальное дробное число {min_fractional}, максимальное дробное число {max_fractional} ')
print(f'Разница между максимальным и минимальным значением дробной части элементов {max_numbers - max_fractional}')
