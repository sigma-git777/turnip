import random
binary = []  # список двоичного представления
number = int(input('Введите число \n'))
if number == 0:
    print('Число в двоичном равно 0')
while number > 0:
    binary.insert(0, number % 2 )
    number = number // 2
binary_int = int(''.join(map(str, binary))) # преобразование в строку двоичного представления
print('Число в двоичном представлении', binary_int)
