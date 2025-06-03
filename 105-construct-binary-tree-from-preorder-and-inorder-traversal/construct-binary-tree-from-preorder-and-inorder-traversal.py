# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTree(pre, ino):
            if len(ino)==0:
                return None
            
            node = TreeNode(pre[0])
            root = pre[0]
            # pre = pre[1:]
            i = 0
            while i < len(ino) and ino[i] != root:
                i+=1

            node.left = buildTree(pre[1:i+1], ino[:i])
            node.right = buildTree(pre[i+1:], ino[i+1:])

            return node
        return buildTree(preorder, inorder)

            
