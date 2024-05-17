class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        answer = [0]*n
        mono_stack = []
        #intialzation a pointer
        #in monotonicity question, creating pointers and  using while loops is common
        i = 0
        while i < n:
            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                poppedT, poppedI = mono_stack.pop()
                answer[poppedI] = i - poppedI
            mono_stack.append((temperatures[i],i))
            i +=1

        return answer
