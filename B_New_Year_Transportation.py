n,goto = map(int, input().split())
portals = list(map(int, input().split()))

cell = 1
while cell<goto:
    if cell >=n:
        print("NO")
        break

    cell += portals[cell-1]
    if cell == goto:
        print("YES")
        break
else:
    print("NO")