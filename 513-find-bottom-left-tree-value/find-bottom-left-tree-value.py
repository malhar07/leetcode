# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = [-1,-1]
        def helper(root, height):
            if not root:
                return
            if height>res[1]:
                res[0] = root.val
                res[1] = height
            helper(root.left, height+1)
            helper(root.right, height+1)
        helper(root, 1)
        return res[0]
            