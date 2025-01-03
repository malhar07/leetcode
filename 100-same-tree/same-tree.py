# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not self.check(p,q):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # stack1 = [p]
        # stack2 = [q]

        # if not p and not q:
        #     return True
        
        # while stack1 and stack2:
        #     root1 = stack1.pop()
        #     root2 = stack2.pop()
        #     if not self.check(root1, root2):
        #         return False
        #     else:
        #         if root1:
        #             stack1.append(root1.left)
        #             stack1.append(root1.right)

        #             stack2.append(root2.left)
        #             stack2.append(root2.right)
        # return True
    
    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return True
        return False
        
