# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def create(left, right):
            nonlocal preorder_ind
            if right<left:
                return None
            
            root = TreeNode(preorder[preorder_ind])
            

            # ind = 0
            # while inorder[ind] != preorder[preorder_ind]:
            #     ind+=1
            preorder_ind+=1

            root.left = create(left, dict1[root.val]-1)
            root.right = create(dict1[root.val]+1, right)

            return root
        dict1 = {}

        for ind, num in enumerate(inorder):
            dict1[num] = ind
        
        preorder_ind = 0
        left = 0
        right = len(inorder)-1

        return create(left, right)

