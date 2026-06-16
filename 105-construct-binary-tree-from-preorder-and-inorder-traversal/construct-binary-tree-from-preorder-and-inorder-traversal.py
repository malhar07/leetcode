# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.ind = 0
        def build( pre, inord):
            if not inord:
                return None

            curr_val = pre[self.ind]
            self.ind+=1

            node = TreeNode(curr_val)

            root_ind = 0
            while inord[root_ind] != curr_val:
                root_ind+=1
            

            node.left = build(pre, inord[:root_ind])
            node.right = build(pre, inord[root_ind+1:])
            return node
        return build(preorder, inorder)
