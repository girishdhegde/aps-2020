import math
def foo():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        y = list(map(int,input().split()))

        pos_x_lookup = [0 for i in range(100000)]
        neg_x_lookup = [0 for i in range(100000)]
        pos_y_lookup = [0 for i in range(100000)]
        neg_y_lookup = [0 for i in range(100000)]

        pos_x = []
        neg_x = []
        pos_y = []
        neg_y = []

        tri = 0
        mul1 = n 
        mul2 = m
        flag = 0

        for num in x:
            if num < 0:
                n = abs(num)
                neg_x.append(n)
                neg_x_lookup[n] = 1

            elif num > 0:
                pos_x.append(num)
                pos_x_lookup[num] = 1

            else:
                mul1 = n - 1
                flag = 1


        for num in y:
            if num < 0:
                n = abs(num)
                neg_y.append(n)
                neg_y_lookup[n] = 1

            elif num > 0:
                pos_y.append(num)
                pos_y_lookup[num] = 1
            else:
                mul2 = m - 1
                flag = 1

        if flag:
            tri = mul2 * mul1
            
        # limit = 100000 * 100000
        for p in pos_x:
            for n in neg_x:
                # if p == n:
                #     if pos_y_lookup[p]:
                #         tri += 1
                #     if neg_y_lookup[p]:
                #         tri += 1
                        
                    
                # else:
                    pro = p * n 
                    y_req = (math.sqrt(pro))
                    if not y_req % 1:
                        yi = int(y_req)
                        tri += pos_y_lookup[yi] + neg_y_lookup[yi]
                        # if pos_y_lookup[yi]:
                        #     tri += 1
                        # if neg_y_lookup[yi]:
                        #     tri += 1
                            
                # print("Y", p, n, y_req)
                    # tri += 1 if y_req in pos_y else 0
                    # tri += 1 if y_req in neg_y else 0
                # print("tri:", tri)

        # print("+", pos_y)
        # print("-", neg_y)
        for p in pos_y:
            for n in neg_y:
                # if p == n:
                #     if pos_y_lookup[p]:
                #         tri += 1
                #     if neg_y_lookup[p]:
                #         tri += 1
                
                # else:
                    pro = p * n 
                    x_req = math.sqrt(pro)
                    if not x_req % 1:
                        xi = int(x_req)
                        tri += pos_x_lookup[xi] + neg_x_lookup[xi]
    
                        # if pos_x_lookup[xi]:
                        #     tri += 1
                        # if neg_x_lookup[xi]:
                        #     tri += 1
            # print("X", p, n, x_req)
                    # tri += 1 if x_req in pos_x else 0
                    # tri += 1 if x_req in neg_x else 0
            # print("tri:", tri)
        print(tri)
foo()