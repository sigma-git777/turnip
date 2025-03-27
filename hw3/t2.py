import random
general_list = []  # основной список
couples = []  # список пар чисел
calculated_numbers = int(input('Ведите количество элементов списка \n'))
for x in range(calculated_numbers):
    general_list.append(random.randint(1, 10))
print(general_list)
len_general_list = len(general_list)
for i in range((len_general_list ) // 2):
    product = general_list[i] * general_list[-i - 1]
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