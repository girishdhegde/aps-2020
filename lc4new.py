t = int(input())

for _ in range(t):
    n, p = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    
    flag = 1
    tot = p

    quo = {c: 0 for c in coins}
    
    if n == 1:
        if p % coins[0] == 0:
            print("NO")
        else:
            t = (p // coins[0]) + 1
            print("YES", t)

    else:

        coins = sorted(coins, reverse=True)
        for i, ele in enumerate(coins):
            w = tot % ele
            # print("list, n, ways:", ele, p, w)
            if w == 0:
                quo[ele] = (tot // ele) - 1
                tot = ele

            else:
                flag = 0
                quo[ele] = (tot // ele) + 1
                print("YES", end=' ')

                for k in quo.keys():
                    print(quo[k], end=' ')
                print()
                break

        if flag:
            print("NO")
