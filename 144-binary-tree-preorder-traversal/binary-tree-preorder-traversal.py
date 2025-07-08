# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            if stack:
                curr = stack.pop()
        return res