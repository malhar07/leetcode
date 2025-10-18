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
        node_map = {None:None}
        temp = head
        while head:
            new_node = Node(head.val)
            node_map[head] = new_node
            head = head.next
        new_head = node_map[temp]
        head = temp
        # print(head.val)
        while temp:
            # print(temp.random.val)
            new_head.next = node_map[temp.next]
            new_head.random = node_map[temp.random]

            new_head = new_head.next
            temp = temp.next
        return node_map[head]

