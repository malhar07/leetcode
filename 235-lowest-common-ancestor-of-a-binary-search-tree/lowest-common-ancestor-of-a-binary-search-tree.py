# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def helper(root):
        #     if not root:
        #         return 
        #     if root.val > p.val and root.val >q.val:
        #         helper(root.left)
        #     elif root.val < p.val and root.val < q.val:
        #         helper(root.right)
        #     else:
        #         self.res = root
        # self.res = []
        # helper(root)
        # return self.res

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val > p.val and curr.val > q.val:
                stack.append(curr.left)
            elif curr.val < p.val and curr.val < q.val:
                stack.append(curr.right)
            else:
                return curr
            
            