# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(root, num):
            if not root:
                return
            num = num*10 + root.val
            if not root.right and not root.left:
                res.append(num)
            helper(root.left, num)
            helper(root.right, num)
        helper(root, 0)
        return sum(res)