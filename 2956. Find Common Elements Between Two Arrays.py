from collections import defaultdict


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        inNums1 = defaultdict(int)
        inNums2 = defaultdict(int)
        
        for i in nums1:
            inNums1[i] += 1

        for i in nums2:
            inNums2[i] += 1

        count1 = 0
        count2 = 0

        for num, count in inNums1.items():
            if num in inNums2:

                count1 += inNums2[num]
        for num,count in inNums2.items():
            if num in inNums1:
                count2 += inNums1[num]

        return [count2,count1]