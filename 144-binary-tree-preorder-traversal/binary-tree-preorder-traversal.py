# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack = []
        # res = [] 
        # if root:
        #     print(root.val)

        # curr = root
        # while curr or stack:
        #     # print(curr.val)
        #     if curr is not None:
        #         res.append(curr.val)
        #         stack.append(curr)
        #         curr = curr.left
        #     else:
        #         curr = stack.pop()
        #         curr = curr.right
        # return res

        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
        return res