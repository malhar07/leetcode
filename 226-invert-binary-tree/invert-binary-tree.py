# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return 

        else:
            root.left, root.right = root.right, root.left

            if root.left:
                self.helper(root.left)
            if root.right:
                self.helper(root.right)
        