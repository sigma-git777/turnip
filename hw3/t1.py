import random
odd_position_elements_summa = 0  # сумма элементов
elements = []  # основной список
numbers_count = int(input('Ведите количество чисел \n'))
for _ in range(numbers_count):
    elements.append(random.randint(1, 100))
for x in elements[0::2]:
    odd_position_elements_summa+=x
print(elements)
print(elements[0::2])
print('sum of elements', odd_position_elements_summa)