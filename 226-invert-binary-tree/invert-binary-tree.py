# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def helper(root):
        #     if not root:
        #         return 
        #     root.left, root.right = root.right, root.left
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return root
        if not root:
            return None
        stack = [root]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root