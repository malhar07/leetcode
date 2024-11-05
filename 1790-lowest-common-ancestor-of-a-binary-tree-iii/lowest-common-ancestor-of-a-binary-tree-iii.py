"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        dict1 = {}

        while p:
            dict1[p] = 1
            p = p.parent
        while q:
            if q in dict1:
                return q
            q = q.parent