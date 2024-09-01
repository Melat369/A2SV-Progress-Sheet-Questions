def max_alternating_subsequence_sum(test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        max_sum = 0
        current_sum = a[0]
        
        for i in range(1, n):
            if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
                current_sum += a[i]
            else:
                max_sum += current_sum
                current_sum = a[i]
        
        max_sum += current_sum
        results.append(max_sum)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = max_alternating_subsequence_sum(test_cases)

# Output results
for result in results:
    print(result)