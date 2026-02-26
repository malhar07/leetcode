# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def depth(level, root):
            if not root:
                return
            self.res = max(level, self.res)

            depth(level+1, root.left)
            depth(level+1, root.right)
        depth(1, root)
        return self.res

