class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        a = {}
        count = 0
        for num in nums:
            a[num] = a.get(num,0) + 1

        for num in nums:
            if a.get(num + diff) and a.get(num+diff*2):
                count += 1
        return count

