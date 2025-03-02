# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # def helper(root, _sum):
        #     if not root:
        #         return False
        #     if _sum+root.val == targetSum and not root.left and not root.right:
        #         return True

        #     left = helper(root.left, _sum+root.val)
        #     right = helper(root.right, _sum+root.val)
        #     return left or right

        # if not root:
        #     return False
        # return helper(root,0)
        if not root:
            return False
        stack = [(root,0)]
        while stack:
            curr, _sum = stack.pop()
            if curr.val+_sum == targetSum and not curr.left and not curr.right:
                return True
            if curr.left:
                stack.append((curr.left,curr.val+_sum))
            if curr.right:
                stack.append((curr.right,curr.val+_sum))
        return False