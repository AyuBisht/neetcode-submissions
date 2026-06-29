"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hashCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = hashCopy[cur]
            copy.next = hashCopy[cur.next]
            copy.random = hashCopy[cur.random]
            cur = cur.next
        
        return hashCopy[head]

        