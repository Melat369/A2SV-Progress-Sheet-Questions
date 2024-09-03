# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deq = deque()

        while head:
            deq.append(head.val)
            head = head.next
        
        if len(deq) == 1:
            return True

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False
        
        return True

        