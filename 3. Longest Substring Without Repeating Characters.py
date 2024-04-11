class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        seen = {}
        length = 0
        for r in range(len(s)):
            curr_char = s[r]
            if curr_char in seen and seen[curr_char]>=l:
                l = seen[curr_char] + 1
            seen[curr_char] = r
            length = max(length,r-l+1)
            
        return length

