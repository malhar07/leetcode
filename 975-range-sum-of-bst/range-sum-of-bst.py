# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if low<=root.val<=high:
                return left+right+root.val
            return left+right
        return helper(root)
