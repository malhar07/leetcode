# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def helper(root):
        #     if not root:
        #         return
        #     nonlocal res

        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        
        # return res

        res = []
        stack = [root]
        curr = root

        curr = stack.pop()
            

        while stack or curr:
            if stack:
                curr = stack.pop()
            while curr:
                if curr.right:
                    stack.append(curr.right)
                res.append(curr.val)
                curr = curr.left
        print(res)
        return res

               
