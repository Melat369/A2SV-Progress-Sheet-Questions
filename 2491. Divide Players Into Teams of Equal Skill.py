class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        totPlayers = len(skill)
        if totPlayers % 2 != 0:
            return -1


        skill.sort()
        totalTeams = totPlayers // 2
        l,r = 0 , len(skill)-1
       
        chemistry = 0
        while l<r:
            sums = skill[l]+skill[r]
            if sums != skill[l+1] + skill[r-1]:
                return -1

            
            chemistry += (skill[l]*skill[r])
            l+=1
            r-=1
        return chemistry 