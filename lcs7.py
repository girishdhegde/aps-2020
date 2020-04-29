import math
def foo():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        y = list(map(int,input().split()))

        

        pos_x = [p for p in x if p > 0]
        neg_x = [abs(n) for n in x if n < 0]
        pos_y = [p for p in y if p > 0]
        neg_y = [abs(n) for n in y if n < 0]

        tri = 0
        mul1 = n 
        mul2 = m
        if len(pos_x) + len(neg_x) < n:
            mul1 = n - 1
            if len(pos_y) + len(neg_y) < m:
                mul2 = m - 1
            tri = mul1 * mul2

        elif len(pos_y) + len(neg_y) < m:
            mul2 = m - 1
            tri = mul1 * mul2


        
        # if 0 in x:
        #     mul1 = n - 1
        #     if 0 in y:
        #         mul2 = m - 1
        #     tri = mul1 * mul2

        # elif 0 in y:
        #     mul2 = m - 1
        #     tri = mul1 * mul2
        #     tri = (m - 1) * n

        for p in pos_x:
            for n in neg_x:
                y_req = (math.sqrt(p * n))
                if y_req % 1 == 0:
                    if y_req in pos_y:
                        tri += 1
                    if y_req in neg_y:
                        tri += 1
                    # print("Y", p, n, y_req)
                    # tri += 1 if y_req in pos_y else 0
                    # tri += 1 if y_req in neg_y else 0
                # print("tri:", tri)

        # print("+", pos_y)
        # print("-", neg_y)
        for p in pos_y:
            for n in neg_y:
                x_req = math.sqrt(p * n)
                if x_req % 1 == 0:

                    if x_req in pos_x:
                        tri += 1
                    if x_req in neg_x:
                        tri += 1
                    # print("Y", p, 
                    # print("X", p, n, x_req)
                    # tri += 1 if x_req in pos_x else 0
                    # tri += 1 if x_req in neg_x else 0
                # print("tri:", tri)

        print(tri)
foo()