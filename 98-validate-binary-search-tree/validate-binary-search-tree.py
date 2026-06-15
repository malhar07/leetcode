# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # def validate(root, lower, upper):
        #     if not root:
        #         return True
        #     if not lower<root.val<upper:
        #         return False
        #     return validate(root.left, lower, root.val) and validate(root.right, root.val, upper)
        # return validate(root, -math.inf, math.inf)

        stack = [[root,-math.inf,math.inf]]

        while stack:
            node, lower, upper = stack.pop()
            if not lower<node.val<upper:
                return False
            if node.left:
                stack.append([node.left, lower, node.val])
            if node.right:
                stack.append([node.right, node.val , upper])
        return True