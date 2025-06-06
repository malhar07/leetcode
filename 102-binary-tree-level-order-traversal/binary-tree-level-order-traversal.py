# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # def dfs(root, level):
        #     if not root:
        #         return 
        #     if level == len(res):
        #         res.append([])
        #     res[level].append(root.val)

        #     dfs(root.left, level+1)
        #     dfs(root.right, level+1)
        # dfs(root,0)
        # return res


        q = deque([root])
        temp = []
        res = []
        if not root:
            return []
        while q:
            temp = []
            for _ in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)
        return res


            
