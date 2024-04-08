class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        ans = [[],[]]
        for i in range(1,(10**5)+1):
            lose = 0
            flag = False
            for match in matches:
                if match[1] == i:
                    lose += 1
                if match[0]==i or match[1] == i:
                    flag = True
            if flag:
                if lose == 0:
                    ans[0].append(i)
                elif lose == 1:
                    ans[1].append(i)
        return ans    
        
            