# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(root,level):
        #     if not root:
        #         return
        #     if level == len(res):
        #         res.append(root.val)
        #     else:
        #         res[level] = root.val
        #     dfs(root.left, level+1)
        #     dfs(root.right, level+1)
        # dfs(root,0)
        # return res
        if not root:
            return []
        res = []
        q = deque([(root,0)])

        while q:
            for _ in range(len(q)):
                node,level = q.popleft()
                last_node = node.val

                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
            res.append(last_node)
        return res
