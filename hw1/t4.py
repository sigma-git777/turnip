# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
print('Введите номер четверти от 1 до 4')
n = int(input())
if n == 1:
    print(f'При заданном номере четверти x>0 и y>0')
elif n == 2:
    print(f'При заданном номере четверти x<0 и y>0')
elif n==3:
    print(f'При заданном номере четверти x<0 и y<0')
elif n == 4:
    print(f'При заданном номере четверти x>0 и y<0')
