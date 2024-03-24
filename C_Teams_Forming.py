def min_problems_to_solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    total_problems = 0
    for i in range(0, n, 2):
        total_problems += a[i+1] - a[i]
    return total_problems

print(min_problems_to_solve())
