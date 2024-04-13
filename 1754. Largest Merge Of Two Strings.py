class Solution:
    def largestMerge(self, word1, word2):
        n, m, str1 = len(word1), len(word2), ""

        i, j = 0, 0 

        while i < n and j < m:
            if word1[i:] <= word2[j:]:
                str1 += word2[j]
                j += 1 
            elif word1[i:] > word2[j:]:
                str1 += word1[i]
                i += 1  

        if i < n:
            str1 += word1[i:]

        if j < m:
            str1 += word2[j:]

        return str1 