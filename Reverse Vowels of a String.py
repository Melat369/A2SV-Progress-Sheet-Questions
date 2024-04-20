class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        l, r = 0, len(s_list) - 1
        
        while l < r:
            while l < len(s_list) and s_list[l] not in vowels:
                l += 1
            while r >= 0 and s_list[r] not in vowels:
                r -= 1
            
            if l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
        
        return ''.join(s_list)