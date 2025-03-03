# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dict1 = defaultdict(int)
        res = []
        # self.s = ""

        def helper(root):
            if not root:
                return ""
            toString = ("(" + helper(root.left) + ")" + str(root.val) + "(" + helper(root.right) + ")")
            dict1[toString] += 1
            if dict1[toString] == 2:
                res.append(root)
            return toString

        helper(root)
        return res