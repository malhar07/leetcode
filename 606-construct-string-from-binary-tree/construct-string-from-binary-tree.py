# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def helper(root):
            if not root:
                return
            self.res.append("(")
            self.res.append(str(root.val))
            # self.res += "(" + str(root.val)
            if not root.left and root.right:
                self.res.append("()")
                # self.res += "()"
            helper(root.left)
            helper(root.right)
            # self.res += ")"
            self.res.append(")")
        helper(root)
        return "".join(self.res[1:-1])
        
