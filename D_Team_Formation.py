def PaulosTeamFormation(n, arr):
    arr.sort()  
    count = 0
    left = 0
    right = 0

    while right < n:
        if arr[right] - arr[left] <= 5:
            count = max(count, right - left + 1)
            right += 1
        else:
            left += 1

    return count


n = int(input())
arr = list(map(int, input().split()))


result = PaulosTeamFormation(n, arr)


print(result)