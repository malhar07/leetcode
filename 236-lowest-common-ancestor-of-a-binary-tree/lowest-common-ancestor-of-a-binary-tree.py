# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def helper(root):
            if not root:
                return False
            
            left = helper(root.left)
            right = helper(root.right)

            
            if left and right:
                self.res = root
                return
            elif (left or right) and (root == p or root == q):
                self.res = root
                return
            return left or right or root == p or root == q

        helper(root)
        return self.res