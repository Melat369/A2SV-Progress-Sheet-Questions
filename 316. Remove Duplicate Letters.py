class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        last_idx = [-1]*26
        for i in range(n):
            last_idx[ord(s[i])- ord('a')] = i
        stack = []
        used_arr = [False]*26

        for i in range(n):
            curr = ord(s[i]) - ord('a')
            if used_arr[curr] == True:
                continue

            while stack and stack[-1] > s[i] and last_idx[ord(stack[-1]) - ord('a')] != -1 and last_idx[ord(stack[-1]) - ord('a')] > i:
                used_arr[ ord(stack[-1]) - ord('a') ] = False
                stack.pop()

            if used_arr[curr] == False:
                stack.append(s[i])
                used_arr[curr] = True

        return ''.join(stack)