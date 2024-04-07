def serejaAndDima(cards):
    s = 0
    d = 0
    left = 0
    right = len(cards) - 1

    while left <= right:
        if cards[left] >= cards[right]:
            s += cards[left]
            left += 1
        else:
            s += cards[right]
            right -= 1

        if left <= right:
            if cards[left] >= cards[right]:
                d += cards[left]
                left += 1
            else:
                d += cards[right]
                right -= 1

    return s, d

n = int(input())
cards = list(map(int, input().split()))
sereja_score, dima_score = serejaAndDima(cards)
print(sereja_score, dima_score)