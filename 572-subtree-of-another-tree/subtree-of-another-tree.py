# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def check(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return root1.val == root2.val and check(root1.left,root2.left) and check(root1.right,root2.right)
        # return check(root.left, subRoot)
        def helper(r, s):
            if not r:
                return
            if r.val == s.val:
                if check(r,s):
                    self.res = True
                    return
            helper(r.left,s)
            helper(r.right,s)

        helper(root, subRoot)
        return self.res

            

             
