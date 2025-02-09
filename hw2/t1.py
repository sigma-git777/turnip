# number amount

a = int(input('Enter number \n'))
s = 0
while a>0:
    s = s + (a %10)
    a = a //10
print(f'Sum of digits of a number {s}')