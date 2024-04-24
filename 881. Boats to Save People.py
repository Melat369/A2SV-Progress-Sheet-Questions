import math

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0 , len(people)-1
        boat = 0
        while l<=r:
            ppl = people[l]+people[r]
            if ppl<=limit:
                boat +=1
                l+=1
                r-=1
            elif ppl>limit:
                boat +=1
                r-=1
            else:
                boat += 1
                l+=1

            
        return boat
