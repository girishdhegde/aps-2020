def longest(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    ls = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] in s2[j - 1]:
                ls[i][j] = ls[i - 1][j - 1] + 1
            else:
                ls[i][j] = max(ls[i -1][j], ls[i][j - 1])
    return ls

if __name__ == '__main__':
    s1 = "abcda"
    s2 = "bdabac"
    ls = (longest(s1, s2))
    for row in ls:
        print(row)