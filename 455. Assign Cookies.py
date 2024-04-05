class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        counter = 0
        greed = 0
        supply = 0

        while greed in range(len(g)) and supply in range(len(s)):
            if g[greed] <= s[supply]:
                counter += 1
                greed += 1
            supply += 1
        return counter


        