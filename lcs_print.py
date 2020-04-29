def longest(s1, s2):
    cnt = 0
    sub = []
    l1 = len(s1)
    l2 = len(s2)

    ls = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] in s2[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1

            else:
                ls[i][j] = max(ls[i -1][j], ls[i][j - 1])
            if ls[i][j] > cnt:

                sub.append(s1[i - 1])
                cnt = ls[i][j]
    return sub
s1 = input()
s2 = input()
s1, s2 = [s1, s2] if len(s1) < len(s2) else [s2, s1]
sb = (longest(s1, s2))
print(''.join(sb))