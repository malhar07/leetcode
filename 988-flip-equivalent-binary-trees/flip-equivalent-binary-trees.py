# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
            # return p.val==q.val and check(p.left,q.left) and check(p.right, q.right)
        
        def helper(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            # if check(l,r):#l.val == r.val:
            if l.val == r.val:
                return (helper(l.left,r.left) and helper(l.right,r.right) )or (helper(l.left,r.right) and helper(l.right,r.left))
            else:
                return False
        return helper(root1,root2)