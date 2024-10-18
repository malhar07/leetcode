# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # root = TreeNode()

        left = 0
        right = len(nums)-1
        return self.helper (left, right, nums)


    def helper(self, left, right, nums):
        mid = (left + right)//2

        if right < left:
            return

        curr = TreeNode(nums[mid])
        curr.left = self.helper(left, mid-1, nums)
        curr.right = self.helper(mid+1, right, nums)
        return curr
            
