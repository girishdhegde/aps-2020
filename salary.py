import numpy as np
t = int(input())
for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    w= np.array(w)

    w = np.sort(w)
    # s = set(w)
    steps = 0
    while(w[0] != np.max(w)):
        while(w[0] != w[-1]):
            steps += 1
            w[:-1] = w[:-1] + 1
            print(w)
        w = np.sort(w)
        # s = set(w)


    print(steps)






# t = int(input())
# for i in range(t):
#     n = int(input())
#     w = list(map(int, input().split()))

#     w.sort()
#     s = set(w)
#     steps = 0
#     while(len(s) > 1):
#         while(w[0] != w[-1]):
#             steps += 1
#             w[:-1] = [wi + 1 for wi in w[:-1]]
#             # print(w)
#         w.sort()
#         s = set(w)


#     print(steps)