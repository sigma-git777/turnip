# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('введите число x '))
y = int(input('введтте число y '))
z = int (input('введите число z '))
if not(x or y or z) == (not x) and (not y) and (not z):
    print('истинно')
else:
    print('ложь') 
