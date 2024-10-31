# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, targetSum, 0)
    def helper(self, root, target, tot):
        if not root:
            return
        
        left = self.helper(root.left, target, tot+root.val)
        right = self.helper(root.right, target, tot+root.val)

        if left == None and right == None:
            if root.val + tot == target:
                return True
            else:
                return False
        else:
            if left or right:
                return True
            return False
            # if left == None:
            #     return right
            # if right == None:
            #     return left
            # return left or right
