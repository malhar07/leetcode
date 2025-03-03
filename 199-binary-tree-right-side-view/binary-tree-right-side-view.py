# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def helper(root, level):
            if not root:
                return
            if len(self.res) == level:
                self.res.append(root.val)
            else:
                self.res[level] = root.val
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return self.res