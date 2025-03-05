# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # self.res = 0
        def helper(root,res,fin):
            if not root:
                return 0
            # s+=str(root.val)
            res = res*10+root.val
            if not root.left and not root.right:
                fin+=res
                return fin
            left = helper(root.left,res,fin)
            right = helper(root.right,res,fin)
            return left+right

        return helper(root, 0,0)
        return self.res




        # self.res = 0
        # def helper(root,s):
        #     if not root:
        #         return
        #     s+=str(root.val)
        #     if not root.left and not root.right:
        #         self.res+=int(s)
        #         s = s[:-1]
        #         return
        #     helper(root.left,s)
        #     helper(root.right,s)
        # helper(root,"")
        # return self.res

            