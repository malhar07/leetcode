# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def helper(root, level):
            if not root:
                return 
            if level == len(self.res):
                self.res.append([])
            self.res[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root,0)

        return self.res
            







        # res = []
        # if not root:
        #     return res
        # q = deque([root])

        # while q:
        #     temp = []
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         temp.append(curr.val)

        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #     res.append(temp)
        # return res
            
