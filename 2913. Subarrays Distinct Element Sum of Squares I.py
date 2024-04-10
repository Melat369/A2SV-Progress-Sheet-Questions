class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mapped = {}
        summed = 0
        n = len(nums)
        
        for start in range(n):
            distinct_count = 0
            for end in range(start, n):
                subarray = nums[start:end+1]
                distinct_count = len(set(subarray))
                mapped[distinct_count] = mapped.get(distinct_count, 0) + 1
        
        for count, frequency in mapped.items():
            summed += count ** 2 * frequency

        return summed