# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if (low != None and root.val <= low) or (high != None and root.val >= high):
                return False
            left = helper(root.left, low = low, high = root.val)
            right = helper(root.right, low = root.val, high = high)

            return left and right
        return helper(root, None, None)

            