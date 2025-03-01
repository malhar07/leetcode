# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Top-Down Recurssion
        # def helper(root, depth):
        #     if not root:
        #         return 0 
        #     left = helper(root.left, depth+1)
        #     right = helper(root.right, depth+1)

        #     return max(left,right,depth)
        # return helper(root,1)

        # Botoom-up recurssion
        # def helper(root):
        #     if not root:
        #         return 0
        #     left = helper(root.left)
        #     right = helper(root.right)
        #     return max(left,right)+1
        # return helper(root)

        # Iteration
        if not root:
            return 0
        stack = [(root,1)]
        res = 0
        while stack:
            curr, depth = stack.pop()
            res = max(res,depth)
            if curr.left:
                stack.append((curr.left, depth+1))
            if curr.right:
                stack.append((curr.right, depth+1))
        return res


