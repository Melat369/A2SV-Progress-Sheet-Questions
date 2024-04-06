from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        output = []
        
        for s in strs:
           sorted_s = tuple(sorted(s))
           
           ana[sorted_s].append(s)
        for val in ana.values():
            output.append(val)
        return output


        