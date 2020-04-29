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
        if (len(set(a + b)) > (n+1)):
            print("NO")
        else:
            print('YES')

