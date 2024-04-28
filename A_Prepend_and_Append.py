t = int(input())

for _ in range(t):
    n = int(input())
    timur = input()
    
    
    l, r = 0, n - 1
    count = n
    

    while l < r:
        if timur[l]!=timur[r]:
        
            count = min(count, r-l-1)
            l += 1
            r -= 1
        else:
            break
    print(count)  
