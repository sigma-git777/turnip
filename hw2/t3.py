number = int(input('Enter number \n'))
list_1 = list()
formula = 1
sum_of_numbers =0
for i in range (1, number + 1):
    formula = round((1+1/number)**number, 2)
    list_1.append(formula)
    sum_of_numbers = round(sum_of_numbers + formula, 2)
print(f'List of numbers {list_1}')
print(f'Sum of numbers {sum_of_numbers}')