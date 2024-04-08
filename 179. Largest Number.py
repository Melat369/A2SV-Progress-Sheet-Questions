class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        y = set(nums)
        if y == [0]:
            return [0]
        sorted_nums = sorted(nums, key=lambda x: str(x) + str(nums[0]), reverse=True)
        res = "".join([str(n) for n in sorted_nums])
        return res