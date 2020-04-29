t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    fruits_index = list(map(int, input().split()))
    price = list(map(int, input().split()))
   
    min = float('inf')
    
    fruit_types = set(fruits_index)
    
    for ft in fruit_types:
        p = 0
        # print("ft:", ft)
        temp_fruit = fruits_index.copy()
        temp_price = price.copy()
        pop_cnt = 0
        for idx, (fr, pr) in enumerate(zip(temp_fruit, temp_price)):
            # print("fr:", fr)
            if fr == ft:
                # print("s")
                p += pr
                price.pop(idx - pop_cnt)
                fruits_index.pop(idx - pop_cnt)
                pop_cnt += 1
        
        print("p:", p)
        if p < min:
            min = p
        
    

    print("min price:", min)
        
    