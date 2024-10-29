# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(root):
            if not root:
                return 
            helper(root.left)
            if k-root.val in dict1:
                self.found = True
            dict1[root.val] += 1
            helper(root.right)
        
        self.found = False
        dict1 = defaultdict(int)

        helper(root)
        return self.found