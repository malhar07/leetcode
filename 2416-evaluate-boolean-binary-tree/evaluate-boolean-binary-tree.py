# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return None
            if root.val in [0,1]:
                return root.val
            left = helper(root.left)
            right = helper(root.right)
            if root.val == 2:
                return left or right
            else:
                return left and right
        return bool(helper(root))

