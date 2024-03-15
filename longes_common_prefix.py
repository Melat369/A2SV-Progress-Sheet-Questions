class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        minimum = min(len(s) for s in strs)

        for i in range(minimum):
            current_char = strs[0][i]
            if all(s[i] == current_char for s in strs):
                prefix += current_char
            else:
                break
        return prefix

        
