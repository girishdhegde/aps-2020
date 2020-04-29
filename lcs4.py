# from itertools import combinations

def ways(ele, n):
    result = [0 for i in range(n + 1)]
    result[0] = 1
    for e in ele:
        for i in range(e, n + 1):
            result[i] += result[i - e]
    return result
            
t = int(input())

for case in range(t):
    n, p = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    allcomb = []
    
    # for i in range(1, n + 1):
    #     c = combinations(coins, i)
    #     c = (list(c))
    #     allcomb.extend(c)
    # c = combinations(coins, 1)
    # c = (list(c))
    # allcomb.extend(c)
    allcomb = coins

    flag = 1
    # print(allcomb)
    for i, ele in enumerate(allcomb):
        w =  ways([ele], p)
        # print("list, n, ways:", ele, p, w)
        if w[-1] == 0:
            flag = 0
            print("YES", end=' ')
            # for num in ele:
            #     if num < p:
            #         r = (p % num) + 1
            r =  (p // ele) + 1
            # print("ele, num, r:", ele, ele[0],  r)
            for ij in range(n):
                if ij == i:
                    print(r, end='')
                else:
                    print(0, end='')
                if ij != n -1:
                    print(' ', end='')
            print()
            break

    if flag:
        print("NO")

    # print("#####")
#     else:
#         continue

#     flag = 1


#     if flag == 0:
#         break

# if flag:
#     print("NO")