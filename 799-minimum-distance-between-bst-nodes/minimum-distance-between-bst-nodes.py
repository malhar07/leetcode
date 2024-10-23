# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root):
            if root == None:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        res.sort()
        ans = 100001
        for i in range(len(res)-1):
            ans = min(ans, (res[i+1] - res[i]))
        return ans