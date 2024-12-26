# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def helper(root, curr):
            nonlocal res
            if root == None:
                return 0
            if root.val >= curr:
                res += 1
            
            helper(root.left, max(root.val, curr))
            helper(root.right, max(root.val,curr))
        helper(root, -10001)
        return res

            

        