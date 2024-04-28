



def minimal_seconds(num_segments, str):
 
    red_count = str.count('r')
    green_count = str.count('g')
    yellow_count = str.count('y')

 
    max_count = max(red_count, green_count, yellow_count)
    if max_count == n:
        return 0
    

    return num_segments - max_count

t = int(input())
for _ in range(t):
    
    n, symbol = input().split()
    n = int(n)
    str = input().strip()
 
    print(minimal_seconds(n, str))

