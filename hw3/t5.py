negfib_list = []
calculated_numbers = int(input('Ведите количество элементов списка \n'))
indices = range(-calculated_numbers, calculated_numbers+1)
#print(indices)  
for i in indices:
    if i < 0: # Для отрицательных индексов
        abs_i = abs(i)
        a, b = 0, 1
        for _ in range(abs_i):
            a, b = b, a + b
#        print(a, b)   
        fibo_list  = (-1)**(abs_i + 1) * a
    elif i == 0:
        fibo_list  = 0
    else:  # Для положительных индексов
        a, b = 0, 1
        for _ in range(i):
            a, b = b, a + b
        fibo_list = a
    negfib_list.append(fibo_list)
print(negfib_list)
