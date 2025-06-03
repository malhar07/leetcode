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
            # res = False
            if not r:
                return False
            # if r.val == s.val:
            if check(r,s):
                # res = True
                return True
            left = helper(r.left,s)
            right = helper(r.right,s)
            return left or right

        return helper(root, subRoot)
        # return self.res

            

             
