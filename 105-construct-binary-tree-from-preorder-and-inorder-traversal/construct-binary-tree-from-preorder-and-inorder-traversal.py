# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_dict = {}
        for ind, i in enumerate(inorder):
            node_dict[i] = ind
        index = 0
        def buildTree(left, right):
            nonlocal index
            if left > right:
                return None
            node_val = preorder[index]
            node = TreeNode(node_val)
            index+=1
            i = node_dict[node_val]

            node.left = buildTree(left, i-1)
            node.right = buildTree(i+1, right)

            return node
        return buildTree(0,len(inorder)-1)

            
