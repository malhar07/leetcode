class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {} # 0 OR 1
        visited = set()
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0

                q = deque([node])

                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = 1-color[node]
                            # if node not in visited:
                            q.append(nei)
                        else:
                            if color[nei] == color[node]:
                                return False
        return True