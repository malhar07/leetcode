# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []

        def helper(root, arr):
            if not root:
                return
            if root.left == None and root.right == None:
                arr.append(root.val)
            
            helper(root.left, arr)
            helper(root.right, arr)

        helper(root1, leaves1)
        helper(root2, leaves2)
        return leaves1 == leaves2