# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,_max):
            nonlocal res
            if not root:
                return
            if root.val >= _max:
                res+=1
            _max = max(_max, root.val)
            dfs(root.left, _max)
            dfs(root.right, _max)
        dfs(root,-math.inf)
        return res