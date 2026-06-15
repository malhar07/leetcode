# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def ancestor(root):
            if not root:
                return False
            left = ancestor(root.left)
            right = ancestor(root.right)

            if left + right + (root == p or root ==q) >= 2:
                self.res = root

            if root == p or root == q or left or right:
                return True

            return False

        ancestor(root)
        return self.res