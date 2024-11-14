# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         self.arr = [] # to store inorder traversal
#         count = 0
#         self.max_count = 0

#         def helper(root, c, prev):
#             if root == None:
#                 return c, prev
#             count = c
#             last_node = prev

#             count, last_node = helper(root.left, count, last_node)

#             if last_node == None or root.val == last_node:
#                 count+1
#                 helper(root.right, count, root.val)
#             else:
#                 if count > self.max_count:
#                     self.max_count = count
#                     self.arr = [last_node]
#                 elif count == self.max_count:
#                     self.arr.append(last_node)
#                 helper(root.right, 1, root.val)
#             return [count, last_node]
#         prev = None
#         helper(root, 0, prev)
#         return self.arr
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return
            
            dfs(node.left)
            
            num = node.val
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                ans.append(num)
            
            dfs(node.right)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        dfs(root)
        return ans