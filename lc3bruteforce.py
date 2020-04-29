def argsort(lst):
    # print("lst:", lst)
    idx = [i for i in range(len(lst))]
    zp  = list(zip(lst, idx))
    zp.sort()
    return list(zip(*zp))[1]

tcase = int(input())
mv = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
price = [25, 50, 75, 100]
total = 0
for case in range(tcase):
    # print("\ncase:", case, tcase, "\n")
    table = [[0 for i in range(4)] for j in range(4)]
    n = int(input())
    s = [0 for i in range(4)]
    for N in range(n):
        movie, time = input().split()
        time = (int(time) // 3) - 1
        movie = mv[movie] 
        table[movie][time] += 1
        s[movie] += 1

    old_table = table.copy()
    # print("old_table:", old_table)
    # print("sum:", s)

    args = []

    for k in range(4):
        table[k] = [table[k][j] * table[k][j] / s[k] for j in range(4) if s[k] != 0] 
        if s[k] == 0:
            table[k] = [0 for i in range(4)]       
        args.append(argsort(table[k])[::-1])


    # print("table:", table)
    # print("args:", args)

    free = 4
    m_t  = [-1 for i in range(4)]
    visited = [-1 for i in range(4)]
    proposed = [[-1 for i in range(4)] for j in range(4)]
    done = [-1 for i in range(4)]
    time = [-1 for i in range(4)]


    itr = 0
    while free:
        nth_mv = done.index(-1)
        jth = 0
        while done[nth_mv] == -1:
            t = args[nth_mv][jth]
            prio = table[nth_mv][t]
            if prio > time[t] and proposed[nth_mv][t] == -1:
                if time[t] == -1:
                    free -= 1
                else:
                    done[m_t[t]] = -1

                time[t] = prio
                m_t[t] = nth_mv
                done[nth_mv] = 1
                proposed[nth_mv][t] = 1
                break

            jth += 1

        # print("iteration:", itr + 1)
        # print("m_t:", m_t)
        # print("nth:", nth_mv)
        # print("proposed:", proposed)
        # print("done:", done)
        # print("time:", time)
        itr += 1

    profit_arr = [old_table[m_t[ij]][ij] for ij in range(4)]
    profit_arr.sort()
    profit = [profit_arr[ijk] * price[ijk] for ijk in range(3, -1, -1)]
    tot = 0     
    for p in profit:
        tot += p if p != 0 else -100
    print(tot)
    total += tot

    # print("m_t:", m_t)
    # print(profit, tot)
    # print(profit_arr)
    # profit_arr.sort()
    # print(profit_arr)
    # print("final table:")

    # for it in range(4):
    #     for jt in range(4):
    #         if m_t[jt] == it:
    #             print("*", old_table[it][jt], end='\t')
    #         else:
    #             print(old_table[it][jt], end='\t')
    #     print("\n")



    # mx = 0
    # max_array = []
    # for idx, row in enumerate(table):
    #     m = max(row)
    #     max_array.append(m)
    #     # mx = m if m > mx else mx




    # max_array.sort()
    # # print("ma:", max_array)
    # profit = 0
    # for i, M in enumerate(max_array):
    #     if M:
    #         profit += M * price[i]
    #     else:
    #         profit -= 100

    # total += profit

    # print(profit)

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