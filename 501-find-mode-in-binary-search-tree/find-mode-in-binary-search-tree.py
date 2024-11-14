# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = [] # to store inorder traversal
        self.count = 0
        self.max_count = 0

        def helper(root):
            if root == None:
                return

            helper(root.left)

            if root.val == self.prev:
                self.count+=1
            else:
                self.prev = root.val
                self.count = 1

            if self.count > self.max_count:
                self.max_count = self.count
                self.arr = [self.prev]
            elif self.count == self.max_count:
                self.arr.append(self.prev)
            


            helper(root.right)
        self.prev = 0
        helper(root)
        return self.arr
