t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = n

    for i in range(n-1):
        if a[i] == a[i+1] or a[i] == a[i+1]-1:
            count -= 1
            # print('YES')
        else:
            print('NO')
            break
    else:
        if count == 1:
            print('YES')
        

   