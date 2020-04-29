t = int(input())
for case in range(t):
    n = int(input())
    sq1 = list(map(int, input().split()))   
    sq2 = list(map(int, input().split()))
    sq1.sort()
    sq2.sort()
    s = 0
    for d in zip(sq1, sq2):
        s += min(d)
    print(s)


