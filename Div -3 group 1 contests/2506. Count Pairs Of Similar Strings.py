class Solution:
    def similarPairs(self, words: List[str]) -> int:
        maper=Counter()
        counter=0
        for current_word in words:
            word="".join(sorted(set(current_word)))
            counter+=maper[word]
            maper[word]+=1
        return counter   














