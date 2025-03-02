# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def check(p,q):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return True 

        def helper(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!= q.val:
                return False
            return p.val == q.val and helper(p.left, q.right) and helper(p.right,q.left)
            # if check(root.left, root.right)
        return helper(root.left, root.right)