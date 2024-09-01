def reachAlice(n, s, a, b):
    if a[0] == 1 and a[s-1] == 1:
        return "YES"

    if a[0] == 1 and a[n-1] == 1 and b[n-1] == 1 and b[s-1] == 1:
        return "YES"

    return "NO"

n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(reachAlice(n, s, a, b))