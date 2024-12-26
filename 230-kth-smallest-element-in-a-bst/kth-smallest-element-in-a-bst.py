# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        count = 1
        res = 0
        
        def dfs(root):
            nonlocal count
            nonlocal res
            if not root or len(arr) == k:
                return
            left = dfs(root.left)
            if count == k:
                res = root.val
            arr.append(root.val)
            count+=1
            
            right = dfs(root.right)
        dfs(root)
        # return arr[k-1]
        return res
            