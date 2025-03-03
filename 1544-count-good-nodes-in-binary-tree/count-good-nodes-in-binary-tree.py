# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0


        def helper(root, prev):
            if not root:
                return 0
            # self.res += root.val >= prev
            curr = root.val >= prev
            left = helper(root.left, max(root.val, prev))
            right = helper(root.right, max(root.val, prev))
            return curr+ left + right
        return helper(root, -math.inf)
        # return self.res

        # res = 0

        # stack = [(root, -math.inf)]
        # while stack:
        #     curr,prev = stack.pop()
        #     if curr.val >= prev:
        #         res+=1
        #     if curr.left:
        #         stack.append((curr.left, max(curr.val,prev)))
        #     if curr.right:
        #         stack.append((curr.right, max(curr.val,prev)))
        # return res

            
        