# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = [] # to store inorder traversal

        def helper(root):
            if root == None:
                return 
            helper(root.left)
            arr.append(root.val)
            helper(root.right)
        helper(root)
        print(arr)

        count = 1
        max_count = 0
        res = []
        for ind, i in enumerate(arr):
            if ind == len(arr)-1 or arr[ind]!=arr[ind+1]:
                if count == max_count:
                    res.append(i)
                elif count> max_count:
                    max_count = count
                    res = [i]
                count=1
            else:
                count+=1
        return res

[1, 2]