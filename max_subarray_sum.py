def maxSubArraySum(a):
    mx = -float('inf')
    tmax = 0 
    for ele in a:
        tmax += ele 
        print(tmax)
        if mx < tmax: 
            mx = tmax
        if tmax < 0:
            tmax = 0              
    return mx 


if __name__ == '__main__':
    a = [1, 2, 3,  -2, 18, 3, -4, 5]
    print(maxSubArraySum(a))