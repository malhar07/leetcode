# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []

        # def level(root, height):
        #     if not root:
        #         return
        #     if height == len(res):
        #         res.append([])
        #     res[height].append(root.val)
        #     level(root.left, height+1)
        #     level(root.right, height+1)
        # level(root, 0)
        # return res

        if not root:
            return []
        res = []

        q = deque([(root,0)])

        while q:
            for i in range(len(q)):
                node, level = q.popleft()
                if level == len(res):
                    res.append([])
                res[level].append(node.val)

                if node.left:
                    q.append((node.left,level+1))
                if node.right:
                    q.append((node.right, level+1))
        return res
                