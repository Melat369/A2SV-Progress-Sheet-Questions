
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        s = 0
        for i in range(len(costs)):
            if costs[i] <= coins:
                s += costs[i]
                if s <= coins:
                    count += 1
                else:
                    break
        return count