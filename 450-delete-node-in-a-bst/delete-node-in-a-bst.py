# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root, key):
            if not root:
                return
            if key > root.val:
                root.right = helper(root.right, key)
            if key < root.val:
                root.left = helper(root.left, key)
            if key == root.val:
                root = delete(root)
            return root
        
        def delete(root):
            if not root.left and not root.right:
                return None
            if not root.left or not root.right:
                return root.left if root.left else root.right
            curr = root.right
            prev = root
            while curr.left:
                prev = curr
                curr = curr.left
            root.val = curr.val
            if  prev == root:
                prev.right = curr.right
            else:
                prev.left = curr.right
            return root

        return helper(root, key)
        
            
            
