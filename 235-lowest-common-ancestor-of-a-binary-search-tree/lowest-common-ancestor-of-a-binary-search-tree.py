# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [-1]

        def helper(root):
            if not root:
                return
            # if root.val == p.val or root.val == q.val:
            #     res[0] = root
            if p.val > root.val and q.val > root.val:
                helper(root.right)
            elif p.val < root.val and q.val < root.val:
                helper(root.left)
            else:
                res[0] = root
        helper(root)
        return res[0]
                