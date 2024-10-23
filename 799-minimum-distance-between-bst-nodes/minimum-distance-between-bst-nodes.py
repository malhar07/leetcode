# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#         res = []

#         def dfs(root):
#             if root == None:
#                 return
            
#             dfs(root.left)
#             res.append(root.val)
#             dfs(root.right)
        
#         dfs(root)
#         res.sort()
#         ans = 100001
#         for i in range(len(res)-1):
#             ans = min(ans, (res[i+1] - res[i]))
#         return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None  # To track the previous node value in the in-order traversal
        self.min_diff = float('inf')  # Initialize the minimum difference to infinity
        
        # In-order traversal helper function
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update the previous node value
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Start the in-order traversal from the root
        inorder(root)
        
        return self.min_diff
