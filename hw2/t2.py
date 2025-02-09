a = int(input('Enter number \n'))
x = list()
y=1
for i in range (1, a+1):
    y = y * i
    x.append(y)
print (f'Set of works {x}')