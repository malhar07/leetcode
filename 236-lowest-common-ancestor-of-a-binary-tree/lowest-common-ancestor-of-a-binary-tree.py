# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.count = 0
        self.res = None
        # found = [False, False]

        def helper(root):
            if not root:
                return False
            left = helper(root.left)
            right = helper(root.right)

            if left and right:
                self.res = root
            

            if root == p or root == q:
                if left or right:
                    self.res = root
                else:
                    return True
            return left or right
        helper(root)
        return self.res
