class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = defaultdict()
        countT = defaultdict()

        for char in s:
            countS[char] = countS.get(char, 0) + 1
            
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        minMove = 0
        for ele in countS:
            if ele not in countT:
                minMove += countS[ele]
            else:
                  minMove += max(countS[ele] - countT[ele], 0)
        return minMove