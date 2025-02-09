n = int(input('Number of elements \n'))
p1 = int(input((f'Enter 1 point in the range from 1 to {n*2+1} \n')))
p2 = int(input((f'Enter 2 point in the range from 1 to {n*2+1} \n')))
ls = list()
for i in range(-n,n+1):
    ls.append(i)
print(*ls)
if 0 < p1 <= n*2+1 and 0 < p2 <= n*2+1 :
    pr = ls[p1-1] * ls[p2-1]
    print(f'Product of two points {pr}')
else:
    print(f'Point 1 and 2 not included in range ')