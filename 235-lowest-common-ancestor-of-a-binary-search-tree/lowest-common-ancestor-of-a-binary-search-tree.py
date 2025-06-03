# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [-1]
        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)

            count = (root.val == p.val or root.val == q.val) + left + right
            if count>1:
                res[0] = root
                return True

            if root.val == p.val or root.val == q.val:
                return True
            return left or right
        dfs(root)
        return res[0]
            