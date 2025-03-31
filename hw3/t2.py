import random
elements = []  # основной список
couples = []  # список пар чисел
numbers_count = int(input('Ведите количество элементов списка \n'))
for x in range(numbers_count):
    elements.append(random.randint(1, 10))
print(elements)
len_general_list = len(elements)
for i in range((len_general_list ) // 2):
    product = elements[i] * elements[-i - 1]
    couples.append(product)
print("Произведения пар:", couples)






# list_length = len(general_list)
# print(list_length)
# for x in range(0, calculated_numbers):
#     calculated_numbers = - (calculated_numbers)
#     summm = general_list[x] + general_list[-n]
#     print(summm)
#     sum_of_elements = list1.append(summm)
#     n -=1
#     print(n)