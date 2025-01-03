# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def helper(root, k):
            # nonlocal res
            if not root or len(res)>=k:
                return
            helper(root.left, k)

            res.append(root.val)

            helper(root.right, k)
        helper(root, k)
        return res[k-1]