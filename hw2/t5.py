import random 
elements = int(input('Number of elements   '))
list_first = list()
list_end = list()
for i in range(1,elements+1):
    list_first.append(i)
print(list_first)
for i in range(len(list_first)):
    random_index =random.randint(0, len(list_first)-1)
    removed = list_first.pop(random_index)
    list_end.append(removed)
print('Mixed list', list_end)
