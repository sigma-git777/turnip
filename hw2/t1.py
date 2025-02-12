# number amount

number = int(input('Enter number \n'))
s = 0
while number>0:
    s = s + (number %10)
    number = number //10
print(f'Sum of digits of number {s}')