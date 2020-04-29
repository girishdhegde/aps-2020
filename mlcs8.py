t, s = list(map(int, input().split()))

for _ in  range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sa = sorted(a)
    sb = sorted(b)


    # if s == 2:
    #     for i in range(n):
    #         if sa[i] != sb[i]:
    #             print("YES")
    #             break
    #     else:
    #         print("NO")

    #     continue

    for i in range(n):
        if sb[i] <= sa[i]:
            print('NO')
            break

    else:

        # a = [1, 2, 3, 3, 3, 4, 2]
        temp = []
        for ai in a:
            if ai not in temp:
                cnt = a.count(ai)
                if cnt & 1:
                    temp.append(ai)

        # b = [1, 3, 4, 8, 9]
        flag = False
        remaining = 0
        for ti in temp:
            if ti not in b:
                remaining += 1
            if remaining == 2:
                flag = True
                break

        if flag:
            print("NO")
        else:
            print('YES')

# # a = [1, 2, 3, 3, 3, 4, 2]
# temp = []
# for ai in a:
#     if ai not in temp:
#         cnt = a.count(ai)
#         if cnt & 1:
#             temp.append(ai)

# # b = [1, 3, 4, 8, 9]
# flag = False
# for ti in temp:
#     if ti not in b:
#         flag = True
#         break

# print(a, "\n", temp, flag)