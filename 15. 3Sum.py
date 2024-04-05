class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = set()
        for num in range(len(nums)):
            l = num + 1
            r = len(nums) - 1
            while l<r:
                if nums[l] + nums[r]+ nums[num] == 0:
                    res = (nums[l], nums[r],nums[num])
                    arr.add(res)
                    l += 1
                elif nums[l] + nums[r]+ nums[num] < 0:

                    l +=1
                elif nums[l] + nums[r]+ nums[num] > 0:
                    r -=1
            
            
        return arr
        
