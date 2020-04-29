from sys import stdin, stdout
lines = stdin.readlines()
t = int(lines[0])
cnt = 1
for _ in range(t):
    n, q = list(map(int, lines[cnt].split()))
    cnt += 1
    a = list(map(int, lines[cnt].split()))
    cnt += 1
    cnt_arr = [bin(ai).count('1') for ai in a]
    
    tcnt = 2
    odd = 0
    for  ac in cnt_arr:
        odd += (tcnt ^ ac) & 1
    evn = n - odd
    
    for _ in range(q):
        p = int(lines[cnt])
        cnt += 1
        pcnt = bin(p).count('1')
        
        if pcnt & 1:
            print(odd, evn)
        else:
            print(evn, odd)
            