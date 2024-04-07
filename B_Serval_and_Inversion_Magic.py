def afterInversionMagic(n, s):
    left = 0
    right = n - 1
    diff_count = 0

    while left < right:
        if s[left] != s[right]:
            diff_count += 1
            if diff_count > 2:
                return "No"
        left += 1
        right -= 1

    if diff_count == 0:
        return "Yes"
    elif diff_count == 2 and s[left] == s[right]:
        return "Yes"
    else:
        return "No"

t = int(input())  

for _ in range(t):
    n = int(input())  
    
    s = input() 
    result = afterInversionMagic(n, s)  
    print(result)  