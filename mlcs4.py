# t = int(input())

# for _ in range(t):
#     n, q = list(map(int, input().split()))
#     a = list(map(int, input().split()))

#     for _ in range(q):
#         x1, x2, y = list(map(int, input().split()))

#         print("next")

#         cnt = 0 

#         temp = a[x1-1: x2+1]
#         for i, p in enumerate(temp[:-1]):
#             print(p, temp[i+1], end=' ')
#             if (y >= p and y < temp[i+1]) or (y < p and y >= temp[i+1]):
#                 cnt += 1
#                 print("yes")
#             print()

#         print("cnt:", cnt)




t = int(input())

for _ in range(t):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for _ in range(q):
        x1, x2, y = list(map(int, input().split()))

        # print("next")

        cnt = 0 

        temp = a[x1-1: x2]
        for i, p in enumerate(temp[:-1]):
            # print(p, temp[i+1], end=' ')
            if (y > p and y < temp[i+1]) or (y < p and y > temp[i+1]):
                cnt += 1                
                # print("yes", end = '')

            if y == p:
                if i != x2:
                    cnt += 1
                    # print("yes", end ='')
            if y == temp[i + 1] and (i + 1) != x1:
                cnt += 1
                # print("yes", end='')
            # print()

        if y == a[x2-1]:
            if x2 != n:
                cnt += 1
                # print(a[x2-1], "yes") 
        # print()

        print("cnt:", cnt)