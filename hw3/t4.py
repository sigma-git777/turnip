import random
y = 0
float_list = [] # список дробных значений элементов списка
general_list = []  # основной список
calculated_numbers = int(input('Ведите количество элементов списка \n'))
for x in range(calculated_numbers):
    general_list.append(round(random.uniform(0, 10),2))
print(general_list)
for x in general_list:
    float_list.append(abs(x) - int(abs(x)))
#   print(abs(x) - int(abs(x)))
min_numbers = round(min(float_list), 2)  # минимальная дробная часть
max_numbers = round(max(float_list), 2)  # максимальная дробная часть
print(f'Минимальное дробное число {min_numbers}, максимальное дробное число {max_numbers} ')
print(f'Разница между максимальным и минимальным значением дробной части элементов {max_numbers - min_numbers}')
