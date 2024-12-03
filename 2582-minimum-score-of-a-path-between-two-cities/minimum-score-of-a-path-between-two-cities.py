class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(1,n+1)}
        for a,b,dist in roads:
            adjlist[a].append(b)
            adjlist[b].append(a)
        visited = set()
        
        def bfs():
            q = deque()
            q.append((1))
            
            visited.add(1)
            while q:
                curr = q.popleft()
                for nei in adjlist[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        bfs()
        dist = 10001

        for road in roads:
            if road[0] in visited:
                dist = min(dist, road[2])
        return dist