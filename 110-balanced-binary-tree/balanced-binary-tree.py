# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True  # An empty tree is balanced

        # Stack to store nodes and an indicator if the node is visited
        stack = [(root, False)]
        heights = {}  # Dictionary to store the height of nodes

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                # After both subtrees have been processed, calculate the height
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                
                # If the node is unbalanced, return False
                if abs(left_height - right_height) > 1:
                    return False

                # Store the height of the current node
                heights[node] = 1 + max(left_height, right_height)
            else:
                # Push the node back onto the stack as visited, and process children
                stack.append((node, True))  # Push node back as "visited"
                stack.append((node.right, False))  # Push right child
                stack.append((node.left, False))  # Push left child

        return True  # If we never found an imbalance, return True


    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     self.isBal = True
    #     self.helper(root)
    #     return self.isBal
    
    # def helper(self, root):
    #     if root == None:
    #         return 0
        
    #     left = self.helper(root.left)
    #     right = self.helper(root.right)

    #     if abs(left-right) > 1:
    #         self.isBal = False
    #     return max(left,right) + 1

