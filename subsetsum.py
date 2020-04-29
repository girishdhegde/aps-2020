n = 11
ele = [4, 5, 10]
def ways(ele, n):
    result = [0 for i in range(n + 1)]
    result[0] = 1
    for e in ele:
        for i in range(e, n + 1):
            result[i] += result[i - e]
    return result
            
print(ways(ele, n))


# def mask(lst, m):
#     m = m.zfill(len(lst))
#     return list(map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m))))

# def subset_sum(lst, target):
#     out = []
#     for i in range(2**len(lst)):
#         pick = mask(lst, bin(i)[2:])
#         if sum(pick) == target:
#             out.append(pick)

#     return out

# print(subset_sum([4, 5, 10], 12))