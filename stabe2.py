n = int(input())
men_pref   = []
women_pref = []
free_men   = []
free_women = []
count      = []
n_free     = n

def argsort(lst):
    idx = [i for i in range(len(lst))]
    zp  = list(zip(lst, idx))
    zp.sort()
    return list(zip(*zp))[1]
wp = []
for  i in range(n):
    men_pref.append(list(map(int, input().split())))
    free_men.append(1)
for  i in range(n):
    wp.append(list(map(int, input().split())))
    free_women.append(1)
    
women_pref = list(map(list, zip(*wp)))
    
engaged_with = [-1 for i in range(n)]
proposals    = [0 for i in range(n)]
already      = [[1 for j in range(n)] for i in range(n)]

while n_free:
    idx = free_men.index(1)
  
    men_args = argsort(men_pref[idx])
    i = 0
    while i < n and free_men[idx] == 1:

        w_idx = men_args[i]
        if not already[idx][w_idx]:
            i += 1
            continue
        proposals[w_idx] += 1
        already[idx][w_idx] = 0
        women = women_pref[w_idx]
        
        if (free_women[w_idx] == 1): 
            # print(w_idx, "accepts", idx)
            free_men[idx] = 0
            free_women[w_idx] = 0
            engaged_with[w_idx] = idx
            n_free -= 1
            break
            
        else:
            old_idx = engaged_with[w_idx]
            
            if women[idx] < women[old_idx]:
                # print(old_idx, "replaced with ", idx, "by", w_idx)
        
                engaged_with[w_idx] = idx 
                free_men[idx]       = 0
                free_men[old_idx]   = 1
                break
            # else:
                # print(w_idx, "rejects", idx)
            
        i += 1
            
q = int(input())
# print(proposals)

for i in range(q):
    w = int(input())
    print(proposals[w - 1])

# print(engaged_with)