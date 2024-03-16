class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s = set(nums)
        key = 0
        val = 0

        for num in s:
            n = nums.count(num)
            if n>1:
                key += n//2
                val += n%2
            else:
                val += 1
        return[key,val]