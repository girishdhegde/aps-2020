
def wPrefersM1OverM(prefer, w, m, m1): 
    for i in range(N): 
        if (prefer[w][i] == m1): 
            return True
        if (prefer[w][i] == m): 
            return False

def stableMarriage(prefer): 
      
    global count
    wPartner = [-1 for i in range(N)]  
    mFree = [False for i in range(N)] 
  
    freeCount = N 
  
    while (freeCount > 0): 
          
        m = 0
        while (m < N): 
            if (mFree[m] == False): 
                break
            m += 1
  
        i = 0
        while i < N and mFree[m] == False: 
            w = prefer[m][i] 
            count[w - N] += 1
  
            if (wPartner[w - N] == -1): 
                wPartner[w - N] = m 
                mFree[m] = True
                freeCount -= 1
  
            else:  
                  
                m1 = wPartner[w - N] 
  
    
                if (wPrefersM1OverM(prefer, w, m, m1) == False): 
                    wPartner[w - N] = m 
                    mFree[m] = True
                    mFree[m1] = False
            i += 1
  


    print("Woman ", " Man") 
    for i in range(N): 
        print(i, "\t", wPartner[i]) 

n = int(input())
N = n
men_pref   = []
women_pref = []
free_men   = []
free_women = []
count      = []
n_free     = n
for  i in range(n):
    men_pref.append(list(map(int, input().split())))
    free_men.append(1)
for  i in range(n):
    women_pref.append(list(map(int, input().split())))
    count.append(0)
# Driver Code 
prefer = []
prefer.extend(men_pref)
prefer.extend(women_pref)
# print(prefer) 
stableMarriage(prefer) 
q = int(input())
for i in range(q):
    w = int(input())
    print(count[w - 1] - N)


