n,m = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ans = []
l = 0
for i in range (len(arr2)):
    while l< len(arr1) and arr2[i] > arr1[l]:
        l += 1
    ans.append(l)
print(*ans)