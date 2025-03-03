# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = []

        def helper(root, rank, depth):
            if not root:
                return
            if depth == len(level):
                level.append([])
            level[depth].append(rank)
            helper(root.left, rank*2, depth+1)
            helper(root.right, rank*2+1, depth+1)
        helper(root, 1, 0)
        res = 1
        print(level)
        for l in level:
            if len(level) >= 2:
                res = max(res, l[-1]-l[0]+1)
        return res