# 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

import math

print('Введите координаты точки A')
xA = int(input('x1 = '))
yA = int(input('y1 = '))
print('Введите координаты точки B')
xB = int(input('x2 = '))
yB = int(input('y2 = '))
s = math.sqrt(((xB - xA) ** 2) + ((yB-yA)** 2))
print(f'Растояние между точками A и B в 2D пространстве = {s}')
