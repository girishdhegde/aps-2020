import math
def foo():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        y = list(map(int,input().split()))

        flag = 0
        mul1 = n
        mul2 = m
        pos_x = []
        neg_x = []
        pos_x_sq = []
        neg_x_sq = []
        pos_y = []
        neg_y = []
        pos_y_sq = []
        neg_y_sq = []

        for num in x:
            sq = num * num
            if num < 0:
                neg_x.append(abs(num))
                neg_x_sq.append(num * num)

            elif num > 0:
                pos_x.append(num)
                pos_x_sq.append(num * num)
            else:
                mul1 = n - 1
                flag = 1


        for num in y:
            # sq = num * num
            if num < 0:
                neg_y.append(abs(num))
                neg_y_sq.append(num * num)

            elif num > 0:
                pos_y.append(num)
                pos_y_sq.append(num * num)
            else:
                mul2 = m - 1
                flag = 1

        
        tri = 0

        if flag:
            tri = mul1 * mul2

        # print("aftere:", tri)
        for p in pos_x:
            for n in neg_x:
                y_req = (p * n)
                if y_req in pos_y_sq:
                    tri += 1
                if y_req in neg_y_sq:
                    # tri += 1
                    print("Y", p, n, y_req)
                    # tri += 1 if y_req in pos_y else 0
                    # tri += 1 if y_req in neg_y else 0
                # print("tri:", tri)

        # print("+", pos_y)
        # print("-", neg_y)
        for p in pos_y:
            for n in neg_y:
                x_req = (p * n)
                if x_req in pos_x_sq:
                    tri += 1
                if x_req in neg_x_sq:
                    tri += 1
                    # print("Y", p, 
                    # print("X", p, n, x_req)
                    # tri += 1 if x_req in pos_x else 0
                    # tri += 1 if x_req in neg_x else 0
                # print("tri:", tri)

        print(tri)
foo()