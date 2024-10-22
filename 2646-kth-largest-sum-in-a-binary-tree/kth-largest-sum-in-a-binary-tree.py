# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        level = []
        res = []
        sum1 = 0

        while True:
            sum1=0
            while stack:
                curr = stack.pop()
                sum1+=curr.val
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            stack = level.copy()
            level = []
            res.append(sum1)
            if len(stack) == 0:
                break
        if k > len(res):
            return -1
        res.sort(reverse = True)
        print(res)
        return res[k-1]

