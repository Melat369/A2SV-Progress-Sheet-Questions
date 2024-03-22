class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        arr = [0] * len(nums)
        for x in nums:
            if x > 0:
                arr[pos] = x
                pos += 2
            else:
                arr[neg] = x
                neg += 2
        return arr