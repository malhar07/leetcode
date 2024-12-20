"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        arr = []
        level = [root]
        temp = []
        def populate():
            nonlocal level, temp
            while level:
                if not level or level[0] == None:
                    return root
                for ind in range(len(level)):
                    if ind != len(level)-1:
                        level[ind].next = level[ind+1]
                    temp.append(level[ind].left)
                    temp.append(level[ind].right)
                
                level = temp
                temp = []
        populate()
        return root


