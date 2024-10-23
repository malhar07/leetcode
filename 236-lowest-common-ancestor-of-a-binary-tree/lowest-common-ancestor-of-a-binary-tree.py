# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def helper(root, p, q):
            if not root:
                return False
        
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if (left and right) or ((left or right) and (root == p or root == q)):
                self.ans = root
                return 
            
            if root == p or root == q or left or right:
                return True
            return False

        helper(root, p, q)
        return self.ans
