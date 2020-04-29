moves = [[4, 4], [7, 1], [1, 7], [2, 8], 
         [8, 2], [7, 3], [8, 4], [4, 8],
         [5, 7], [6, 8], [8, 6], [7, 7], 
         [8, 8], [3, 3], [1, 5], [5, 1],
         [4, 2], [3, 1], [1, 3], [2, 2],
                                 [1, 1]]
t = int(input())
for _ in range(t):
    cnt = 21
    ro, co = list(map(int, input().split()))
    flag = True

    if ro > co:
        rn = ro - 1
        cn = co + 1
        while(rn != cn):
            rn -= 1
            cn += 1
        if rn != 4:
            cnt += 1
            print(cnt)
            print(rn, cn)
            flag = False

    elif co > ro:
        rn = ro + 1
        cn = co - 1
        while(rn != cn):
            rn += 1
            cn -= 1
        if rn != 4:
            cnt += 1
            print(cnt)
            print(rn, cn)
            flag = False

    if flag:
        print(cnt)

    for mv in moves:
        print(*mv)


