# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkNode(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return True
        
        def helper(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if checkNode(p,q):
                return helper(p.left,q.left) and helper(p.right,q.right)
            else:
                return False
        return helper(p,q)