n = int(input())
w = []


for  i in range(n):
    w.append(list(map(int, input().split())))
out = ([ sum(x) for x in zip(*w) ])
flag = 0
for i, men in enumerate(out):
    if men == -n:
        print(i + 1)
        flag = 1
if not flag:
    print(-1)


n = int(input())
w = []

def intersection(lst1, lst2): 
    same = [ele for ele in lst1 if ele in lst2] 
    return same
single = []

for  i in range(n):
    w.append(list(map(int, input().split())))
    single.append([])
    for i, e in enumerate(w[-1]):
        if e == -1:
            single[-1].append(i)
same = single[0]
for lst in single[1:-1]:
    same = intersection(same, lst)

if len(same) == 0:
    print(-1)
else:
    for men in same:
        print(men + 1)
