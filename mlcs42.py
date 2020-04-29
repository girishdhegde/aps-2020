
t = int(input())

for _ in range(t):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for _ in range(q):
        x1, x2, y = list(map(int, input().split()))

        cnt = 0 

        for i in range(x1-1, x2-1):
            print("i:", i, a[i])
            if (a[i] <= y and a[i+1] >= y) or (a[i] >= y and a[i+1] <= y):
                cnt += 1



        print("cnt:", cnt)