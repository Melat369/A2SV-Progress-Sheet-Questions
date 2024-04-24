class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        
        p,t = 0,0
        matched = set()
        
        while p < len(players) and t < len(trainers):
            if players[p]<=trainers[t] and t not in matched:
                count += 1
                matched.add(t)
                p+=1
            t+=1
            

        return count
            
