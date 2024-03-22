class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:    
        count = 0
        #to check the next element in advance
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i > 0 and nums[i+1] < nums[i-1]:
                    #checking if it is a middle element
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return count <= 1
                
