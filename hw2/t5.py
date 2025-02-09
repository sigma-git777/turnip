import random 
n = int(input('Number of elements   '))
ls = list()
lsf = list()
for i in range(1,n+1):
    ls.append(i)
print(ls)
for i in range(len(ls)):
    random_index =random.randint(0, len(ls)-1)
    removed = ls.pop(random_index)
    lsf.append(removed)
print('Mixed list', lsf)
