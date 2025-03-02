# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root1 and not root2:
        #     return None
        
        # def helper(p,q):
        #     if not p and not q:
        #         return None
        #     if not p:
        #         return q
        #     if not q:
        #         return p
        #     p.left = helper(p.left, q.left)
        #     p.right = helper(p.right, q.right)
        #     p.val = p.val+q.val
        #     return p
        # return helper(root1, root2)

        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        
        stack = [(root1, root2)]

        while stack:
            p,q = stack.pop()

            if not p.left and q.left:
                p.left = q.left
            elif p.left and q.left:
                p.left.val+=q.left.val
                stack.append((p.left,q.left))

            if not p.right and q.right:
                p.right = q.right
            elif p.right and q.right:
                p.right.val += q.right.val
                stack.append((p.right,q.right))
        return root1

            





        