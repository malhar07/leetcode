# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def goodNodes(root, curr_max):
            res = 0
            if not root:
                return 0
            if root.val >= curr_max:
                res += 1
            left = goodNodes(root.left, max(curr_max, root.val))
            right = goodNodes(root.right, max(curr_max, root.val))

            return left+right+res
        return goodNodes(root, root.val)