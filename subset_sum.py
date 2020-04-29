n = 75
ele = [3, 5, 10]
result = [0 for i in range(n + 1)]
result[0] = 1
out = []
# def ways(ele, )
old  = [0 for i in range(n + 1)]
old_temp = [[] for i in range(n + 1)]
bfore = 0
for e in ele:
    old_temp[e] = [e]
    for i in range(e, n + 1):
            result[i] += result[i - e]
            if result[i] > old[i] and i not in ele:
                temp = []
                ptr = i
                temp.append(ptr)
                while ptr >= e:
                    ptr = ptr - e

                    temp.append(ptr)
                # temp.extend(old_temp[ptr])
                old_temp[i].append(temp)
                # out.append(temp)
                old[i] = result[i]



final = old_temp[-1]
print(final)
print(result)

# for values in final:
#     print("\n")
#     for i,v in enumerate(values[:-1]):
#         print(v - values[i + 1], end=',')

# print(final[-1][-1])
# print(result)
# # print(out)
# print(old_temp)