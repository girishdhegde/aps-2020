t = int(input())
for case in range(t):
    x, y, k, n = list(map(int, input().split()))
    req_pages = x - y
    flag = False
    for i in range(n):
        p, c = list(map(int, input().split()))
        if c <= k and p >= req_pages:
            flag = True
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")