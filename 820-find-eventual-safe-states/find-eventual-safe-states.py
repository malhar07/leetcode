# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         adjlist = {node:[] for node in range(len(graph))}
#         terminal = set()
#         for node, nei in enumerate(graph):
#             for n in nei:
#                 adjlist[node].append(n)
#         for i in range(len(graph)):
#             if adjlist[i] == []:
#                 terminal.add(i)
#         path = set()
#         def dfs(node):
#             if node in terminal:
#                 return True
#             if node in path:
#                 return False
#             path.add(node)
#             isSafe = True
#             for nei in adjlist[node]:
#                 isSafe = dfs(nei) and isSafe
#                 if not isSafe:
#                     return False
#             path.remove(node)
#             if isSafe:
#                 terminal.add(node)
#             return isSafe
#         res = []
#         for i in range(len(graph)):
#             if i in terminal:
#                 res.append(i)
#             elif dfs(i):
#                 res.append(i)
#         return res
        
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if state[node] == 1:
                return False  # cycle detected
            if state[node] == 2:
                return True   # already marked safe

            state[node] = 1  # mark as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2  # mark as safe
            return True

        return [i for i in range(n) if dfs(i)]
