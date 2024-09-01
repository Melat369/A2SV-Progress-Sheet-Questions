class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line_sweep_arr = [0] * (len(s)+1)       
        for start,end,direction in shifts:
            if direction==0:
                direction = -1
            line_sweep_arr[start] += direction
            line_sweep_arr[end+1] -= direction  
        
        accumulated = 0                        
        res = []
        for i in range(len(s)):
            accumulated += line_sweep_arr[i]    
            chr_num = ord(s[i])-ord('a')        
            chr_num = (chr_num+accumulated)%26  
            res.append(chr(chr_num+ord('a')))   
        return ''.join(res)