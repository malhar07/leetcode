# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        def helper(p,q):
            if not p and not q:
                return None
            if not p:
                return q
            if not q:
                return p
            p.left = helper(p.left, q.left)
            p.right = helper(p.right, q.right)
            p.val = p.val+q.val
            return p
        return helper(root1, root2)



        