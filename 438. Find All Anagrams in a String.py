class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp = Counter(p)
        window_size = len(p)
        anagram = []

        for end in range(0,len(s)-window_size+1):
            portion = Counter(list(s[end:end+window_size]))
            if portion == countp:
                anagram.append(end)
               
        return anagram
