elements = int(input('Number of elements \n'))
point_first = int(input((f'Enter 1 point in the range from 1 to {elements*2+1} \n')))
point_second = int(input((f'Enter 2 point in the range from 1 to {elements*2+1} \n')))
list_1 = list()
for i in range(-elements,elements+1):
    list_1.append(i)
print(*list_1)
if 0 < point_first <= elements*2+1 and 0 < point_second <= elements*2+1 :
    work = list_1[point_first-1] * list_1[point_second-1]
    print(f'Product of two points {work}')
else:
    print(f'Point 1 or 2 not included in range ')