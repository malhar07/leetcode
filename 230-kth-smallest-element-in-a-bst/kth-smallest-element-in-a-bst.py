# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k
        def helper(root):

            if not root:
                return None
            
            left = helper(root.left)

            self.k-=1
            if self.k == 0:
                self.res =  root.val

            right = helper(root.right)

            # if left != None:
            #     return left
            # elif right != None:
            #     return right
            # return None
        helper(root)
        return self.res
