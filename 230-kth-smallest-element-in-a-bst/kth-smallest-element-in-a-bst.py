# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0
        
        def inorder(root):
            if not root:
                return 0
            
            left = inorder(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val

            right = inorder(root.right)

        inorder(root)
        return self.res