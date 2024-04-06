class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       ss = sorted(list(s))
       tt = sorted(list(t))
       if ss == tt:
            return True
    