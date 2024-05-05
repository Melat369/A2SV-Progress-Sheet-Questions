class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # take the first charachter then find the last occurence of that char and count the number of 
        # elements that are different from the character that we are counting and if the k is less than of
        # the number of diffrent characters that are in between then.... I will think about it
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):

    
            count[s[r]] = 1 + count.get(s[r],0)
            while(r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l + 1)
        return res