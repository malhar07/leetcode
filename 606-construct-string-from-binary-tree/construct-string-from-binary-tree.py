# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def helper(root):
            nonlocal res
            if not root:
                return
            res+="("
            res+=str(root.val)

            helper(root.left)
            if not root.left and root.right:
                res+="()"
            helper(root.right)

            res+=")"
        helper(root)
        return res[1:-1]