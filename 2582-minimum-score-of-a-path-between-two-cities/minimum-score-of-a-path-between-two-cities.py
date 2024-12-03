class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(1,n+1)}
        for a,b,dist in roads:
            adjlist[a].append((b,dist))
            adjlist[b].append((a,dist))
        visited = set()
        
        self.dist = 10001
        def bfs():
            q = deque()
            q.append((1))
            
            visited.add(1)
            while q:
                curr = q.popleft()
                for nei, d in adjlist[curr]:
                    self.dist = min(self.dist, d)
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            return self.dist

        return bfs()
        # dist = 10001

        # for road in roads:
        #     if road[0] in visited:
        #         dist = min(dist, road[2])
        # return dist