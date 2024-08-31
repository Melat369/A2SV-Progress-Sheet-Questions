n = int(input())
likes = list(map(int, input().split()))

for i in range(1,n+1):
    A = i
    B = likes[A-1]
    C = likes[B-1]
    if likes[C-1]==A:
         print("YES")
         break
else:
    print("NO")
