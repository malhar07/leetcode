# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # def helper(root):
        #     if not root:
        #         return 0
        #     left = helper(root.left)
        #     right = helper(root.right)
        #     if low<=root.val<=high:
        #         return left+right+root.val
        #     return left+right
        # return helper(root)

        res = 0
        if not root:
            return res
        stack = [root]
        while stack:
            curr = stack.pop()
            if low<=curr.val<=high:
                res+=curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res
