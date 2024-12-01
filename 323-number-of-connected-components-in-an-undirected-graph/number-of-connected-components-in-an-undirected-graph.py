class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {}
        visited = set()
        for i in range(n):
            adjlist[i] = []
        
        for edge in edges:
            adjlist[edge[0]].append(edge[1])
            adjlist[edge[1]].append(edge[0])
        
        def bfs(node):
            if node in visited:
                return 0
            q = deque()
            q.append(node)
            visited.add(node)

            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    for nei in adjlist[curr]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            return 1

        
        res=0
        for i in range(n):
            res += bfs(i)
        return res