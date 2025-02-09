n = int(input('Enter number \n'))
x = list()
y=1
s=0
for i in range (1, n+1):
    y = round((1+1/n)**n, 2)
    x.append(y)
    s = round(s + y, 2)
print(f'List of numbers {x}')
print(f'Sum of numbers {s}')