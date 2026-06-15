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
        if not head:
            return
        head2 = ListNode(head.val)

        node_dict = {head:head2, None:None}
        temp2 = head2
        temp = head

        while temp.next:
            node = ListNode(temp.next.val)
            temp2.next = node



            temp = temp.next
            temp2 = temp2.next
            node_dict[temp] = temp2

        for key, val in node_dict.items():
            if val:
                val.random = node_dict[key.random]
        return head2

        
