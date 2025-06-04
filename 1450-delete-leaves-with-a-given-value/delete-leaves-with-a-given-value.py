# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root):
            print("kkk")
            if not root:
                return True
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right and root.val == target:
                root.val = -1
                return True
            return False
        dfs(root)
        if root.val == -1:
            return None

        def deleteNodes(root):
            if not root:
                return 
            if root.left and root.left.val == -1:
                root.left = None
            else:
                deleteNodes(root.left)
            if root.right and root.right.val == -1:
                root.right = None
            else:
                deleteNodes(root.right)
            return root
            

        return deleteNodes(root)

