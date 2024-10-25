# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = []
        def helper(root):
            if not root:
                return
            

            s.append("(")
            s.append(str(root.val))
            if not root.left and root.right:
                s.append("()")
            helper(root.left)
                
            if root.right:
                # s.append("(")
                helper(root.right)
            s.append(")")
                # s.append(")")

        
        
        helper(root)
        s = "".join (s)
        return s[1:-1]
        