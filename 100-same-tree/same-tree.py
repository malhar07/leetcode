# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not self.check(p,q):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        if root1.val == root2.val:
            return True
        # return False