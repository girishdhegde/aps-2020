t = int(input())
mv = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
price = [25, 50, 75, 100]
total = 0
for case in range(t):
    table = [[0 for i in range(4)] for j in range(4)]
    n = int(input())
    for N in range(n):
        movie, time = input().split()
        time = (int(time) // 3) - 1
        movie = mv[movie] 
        table[movie][time] += 1

    mx = 0
    max_array = []
    for idx, row in enumerate(table):
        m = max(row)
        max_array.append(m)
        # mx = m if m > mx else mx




    max_array.sort()
    # print("ma:", max_array)
    profit = 0
    for i, M in enumerate(max_array):
        if M:
            profit += M * price[i]
        else:
            profit -= 100

    total += profit

    print(table)
    print(profit)

print(total)


# 5
# 12
# A 3
# B 12
# C 6
# A 9
# B 12
# C 12
# D 3
# B 9
# D 3
# B 12
# B 9
# C 6
# 7
# A 9
# A 9
# B 6
# C 3
# D 12
# A 9
# B 6
# 2
# A 9
# B 6
# 1
# D 12
# 0