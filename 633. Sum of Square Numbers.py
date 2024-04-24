class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        
        while l<= r:
            summed = l*l + r*r
            if summed == c:
                return True
            elif summed < c:
                l+=1
            else:
                r -= 1
        return False
        # newSet = [0, c]
        # for a in newSet:
        #     b = int(math.sqrt(c - a * a))
        #     if a *a + b *b == c:
        #         return True
        # return False

