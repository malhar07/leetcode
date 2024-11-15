# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #put all values in arr

        def helper(root):
            if not root:
                return None
            
            helper(root.left)
            if self.prev != None:
                self.min_diff = min(self.min_diff, root.val-self.prev)
            self.prev = root.val
            helper(root.right)

        
        self.min_diff = 100001
        self.prev = None
        helper(root)
        return self.min_diff
        
        # for i in range(1, len(arr)):
        #     min_diff = min(min_diff, arr[i]-arr[i-1])
        # return min_diff


        
