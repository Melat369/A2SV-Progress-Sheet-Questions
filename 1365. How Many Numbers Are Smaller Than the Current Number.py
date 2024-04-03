class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        sortedd = sorted(nums)

        for i in nums:
            result.append(sortedd.index(i))
        return result
   
           