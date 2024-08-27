n, k = map(int, input().split())
arr = sorted(map(int, input().split()))

if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k <= n:
    x = arr[k-1]
    if k < n and arr[k] == x:
        print(-1)
    else:
        print(x)
else:
    print(-1)
