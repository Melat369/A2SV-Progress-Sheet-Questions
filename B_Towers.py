n = int(input())
sticks = [int(x) for x in input().split()]

for i in sticks:
    longest = {}
    for l in sticks:
        if l in longest:
            longest[l] += 1

        else:
            longest[l] = 1

    maxCount = max(longest.values())
    uniqueLen = len(longest)

print(maxCount,uniqueLen)