# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        levels = []
        temp = []
        levels.append(root)
        while True:
            for i in levels:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            res.append(levels[-1].val)

            if not temp:
                return res
            else:
                levels = temp[:]
                temp = []

