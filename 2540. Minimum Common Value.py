class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = Counter(nums1)
        n2= Counter(nums2)
        arr=[]
        for key,val in n1.items():
            if key in n2:
                arr.append(key)
        arr.sort()
        if len(arr) == 0:
            return -1
        return arr[0]