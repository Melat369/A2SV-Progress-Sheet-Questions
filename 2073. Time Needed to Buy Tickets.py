class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        new=[]
        kk=tickets[k]
        x=0
        for i in range(len(tickets)):
            if tickets[i]<=kk:
                new.append(tickets[i])
            if i > k and tickets[i]>=tickets[k]:
                x+=1
        more=len(tickets)-len(new)
        
        return sum(new)+(more*kk)-x