# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        stack = [(p,q)]
        while stack:
            p,q = stack.pop()
            if not check(p,q):
                return False
            if p:
                stack.append((p.left,q.left))
                stack.append((p.right, q.right))
        return True

            
