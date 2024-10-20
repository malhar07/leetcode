# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # stack = [[root, 1]]
        # depth = 0
        # res=0

        # while stack:
        #     curr, depth = stack.pop()
        #     if curr:
        #         res = max(res, depth)

        #         if curr.left:
        #             stack.append([curr.left, depth+1])
        #         if curr.right:
        #             stack.append([curr.right, depth+1])
        # return res
        return self.helper(root)

    def helper(self, root):
        if root == None:
            return 0
        else:
            left = self.helper(root.left)+1
            right = self.helper(root.right)+1

        return max(left,right)


                