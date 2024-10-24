# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels
        def helper(root, level):
            if level == len(levels):
                levels.append([])
            
            levels[level].append(root.val)
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
        helper(root, 0)
            
        for i in range(len(levels)):
            if i%2 == 1:
                levels[i] = levels[i][::-1]
        return levels