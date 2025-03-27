import random
sum_of_elements = 0  # сумма элементов
odd_position = []  # список из нечетных позиций
general_list = []  # основной список
calculated_numbers = int(input('Ведите количество чисел \n'))
for _ in range(calculated_numbers):
    general_list.append(random.randint(1, 100))
odd_position = general_list[0::2]
for x in odd_position:
    sum_of_elements+=x
print(general_list)
print(odd_position)
print('sum of elements', sum_of_elements)