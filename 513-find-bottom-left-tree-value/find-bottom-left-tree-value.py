# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = None
        self.depth = 1

        def helper(root,d):
            if not root:
                return 
            if d>= self.depth:
                self.res = root.val
                self.depth = d
            helper(root.right, d+1)
            helper(root.left, d+1)
        helper(root,1)
        return self.res