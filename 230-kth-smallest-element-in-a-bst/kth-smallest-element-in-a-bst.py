# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        count = 0
        def dfs(root):
            nonlocal res, count
            if not root:
                return 
            dfs(root.left)
            count += 1
            if count == k:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res
        
