# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = 100001
        self.prev = None

        def helper(root):
            if not root:
                return
            
            helper(root.left)
            if self.prev != None:
                self.res = min(self.res, root.val-self.prev)
            self.prev = root.val
            helper(root.right)
        helper(root)
        return self.res