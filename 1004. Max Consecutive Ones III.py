class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_conseq = 0
       
        for r, num in enumerate(nums):
            k -=1 - num
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                max_conseq = max(max_conseq,r-l+1)

        return max_conseq


         