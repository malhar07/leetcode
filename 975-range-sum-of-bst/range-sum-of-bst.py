# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        tot = 0
    
        def helper( root):
            nonlocal tot
            if not root:
                return 
            if root.val >= low and root.val <= high:
                tot+=root.val
                # helper(root.right)
                # helper(root.left)

            if root.val > low:
                helper(root.left)
            if root.val < high:
                helper(root.right)
        helper(root)
        return tot
            