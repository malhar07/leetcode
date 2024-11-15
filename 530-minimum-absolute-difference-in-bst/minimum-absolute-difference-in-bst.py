# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #put all values in arr
        arr = []
        def helper(root):
            if not root:
                return None
            
            helper(root.left)
            arr.append(root.val)
            helper(root.right)
        helper(root)
        #sort the array
        arr = sorted(arr)
        #check difference of adjacent nodes
        min_diff = 100001
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i]-arr[i-1])
        return min_diff


        
