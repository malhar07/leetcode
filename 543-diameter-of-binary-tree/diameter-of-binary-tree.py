# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        stack = []
        if not root:
            return 0
        else:
            stack.append(root)

            while stack:
                curr = stack.pop()
                left = self.depth(curr.left)
                right = self.depth(curr.right)
                diameter = max(diameter, left + right)
                if left > right:
                    stack.append(curr.left)
                elif right > left:
                    stack.append(curr.right)
                else:
                    return diameter

    
    def depth(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)+1
        right = self.depth(root.right)+1

        return max(left,right)