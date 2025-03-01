# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def helper(root, res):
        #     if not root:
        #         return None
        #     helper(root.left,res)
        #     helper(root.right,res)
        #     res.append(root.val)
        # helper(root,res)
        # return res

        res = []
        def helper(root):
            res = []
            if not root:
                return []
            left = helper(root.left)
            right = helper(root.right)

            res.append(root.val)
            return left+right+res
        return helper(root)

