# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            stack = []
            curr = root
            stack.append((root, 1))
            curr = curr.left
            height = 1
            max_h = 1

            while curr or stack:
                while curr:
                    stack.append((curr, height+1))
                    height += 1
                    max_h = max(max_h, height)
                    curr = curr.left
                if stack:
                    curr, height = stack.pop()
                    curr = curr.right
            return max_h



