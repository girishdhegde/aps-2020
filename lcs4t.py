from collections import defaultdict
import math

t=int(input())

for i in range(t):
    n, total=map(int,input().split())
    coin = []
    values = defaultdict(list)
    y = list(map(int,input().split()))
    for j in range(n):
        coin.append(y[j])
        values[y[j]].append(0)
    coins = []
    for j in range(n):
        if coin[j]!=1:
            coins.append(coin[j])

    print("coins:", coins)

    if(len(coins) == 1):
        if(total%coins[0]==0):
            print("NO")
        else:
            values[coins[0]][0]=math.ceil(total/coins[0])
            print("YES",end=" ")
            x=list(values.values())
            for h in x:
                print(h[0],end=" ")
    else:
        coins=sorted(coins,reverse=True)
        flag=0
        for c in coins:
            if total%c==0:
                d=total/c-1
                values[c][0]=int(d)
                total-=d*c
            else:
                flag=1
                d=math.ceil(total/c)
                values[c][0]=int(d)
                break
                
        if flag==0:
            print("NO")
        else:
            print("YES",end=" ")
            x=list(values.values())
            for h in x:
                print(h[0],end=" ")