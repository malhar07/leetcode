# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels = []

        if not root.left and not root.right:
            return True

        def helper(root, level):
            if not root:
                return
            if level == len(levels):
                levels.append([])
            levels[level].append(root)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)

        for ind in range(len(levels)-1):
            if len(levels[ind]) != 2**ind:
                return False
        print(levels)
        count = len(levels[-1])//2
        rem = len(levels[-1])%2
        i=0
        for i in range(count):
            if not levels[-2][i].left or not levels[-2][i].right:
                return False
        print(i , " i ")
        if rem:
            if not levels[-2][count].left:
                return False
        return True
