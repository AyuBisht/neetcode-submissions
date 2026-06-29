# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()

        while head:
            if id(head) in hashset:
                return True
            hashset.add(id(head))
            head = head.next
        
        return False
        