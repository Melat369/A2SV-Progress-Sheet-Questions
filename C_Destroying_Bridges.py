t = int(input())
test = [tuple(map(int, input().split())) for _ in range(t)]

results = []
for n, k in test:
    if k >= n - 1:
        results.append(1)
    else:
        results.append(n - k)

for result in results:
    print(result)