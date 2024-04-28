n = int(input())
s = input()
remove = 0
l,r = 0, 1
while l<r and r<n:
    if s[l]==s[r]:
        remove += 1
        l+=1
        r+=1
    else:
        l+=1
        r+=1
print(remove)
