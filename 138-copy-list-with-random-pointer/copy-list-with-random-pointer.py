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
        temp = head
        dict1 = {None:None}
        if not head:
            return None
        while temp:
            new_node = Node(temp.val)
            dict1[temp] = new_node
            temp = temp.next
        dummy = dict1[head]
        temp_copy = dummy

        temp = head

        while temp:
            temp_copy.next = dict1[temp.next]
            temp_copy.random = dict1[temp.random]
            temp = temp.next
            temp_copy = temp_copy.next
        return dummy
