class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjlist = {node:[] for node in range(len(graph))}
        terminal = set()
        for node, nei in enumerate(graph):
            for n in nei:
                adjlist[node].append(n)
        for i in range(len(graph)):
            if adjlist[i] == []:
                terminal.add(i)
        path = set()
        def dfs(node):
            if node in terminal:
                return True
            if node in path:
                return False
            path.add(node)
            isSafe = True
            for nei in adjlist[node]:
                isSafe = dfs(nei) and isSafe
                if not isSafe:
                    return False
            path.remove(node)
            if isSafe:
                terminal.add(node)
            return isSafe
        res = []
        for i in range(len(graph)):
            if i in terminal:
                res.append(i)
            elif dfs(i):
                res.append(i)
        return res
        
