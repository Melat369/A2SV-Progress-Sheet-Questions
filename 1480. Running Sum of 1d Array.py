class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        arr = []
        for i in nums:
            summ += i
            arr.append(summ)

        return arr