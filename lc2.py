t = int(input())
for case in range(t):
    n, factor = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    take = 0
    move = [0]
    # dif = []
    # get  = [take]
    r = float('inf')
    for nc in range(n - 1, -1, -1):
        x = (coins[nc] % factor)
        if x:
            move.append(move[n - nc - 1] + (factor - x))
        else:
            move.append(move[n - nc - 1])

    # print("move:", move)

    for c in range(1, n + 1):
        take += coins[c - 1] % factor
        # get.append(take)
        temp = (take - move[n - c])
        if temp > -1:
            r = min([r, temp])
        # dif.append(temp)

    # print("take:", get)
    # print("dif:", dif)

    if r != float('inf'):
        print(r)
    else:
        print(0)



#test
# 2
# 5 7
# 1 14 4 41 1
# 3 9
# 1 10 19


# 1
# 5 7
# 1 14 4 41 1