number = int(input('Enter number \n'))
list_1 = list()
work = 1
for i in range (1, number+1):
    work = work * i
    list_1.append(work)
print (f'Set of works {list_1}')