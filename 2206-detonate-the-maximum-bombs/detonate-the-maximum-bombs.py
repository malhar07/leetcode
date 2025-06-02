class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dist(x1,y1,x2,y2):
            return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        adjlist = defaultdict(list)
        for i in range(len(bombs)):
            for j in range((len(bombs))):
                if i!=j:
                    if dist(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]:
                        adjlist[i].append(j)
        
        
        def dfs(i):
            visited = set([i])
            q = deque([i])

            while q:
                curr = q.popleft()
                for bomb in adjlist[curr]:
                    if bomb not in visited:
                        visited.add(bomb)
                        q.append(bomb)
            return len(visited)

        res = 0

        for i in range(len(bombs)):
            visited = set()
            res = max(res,dfs(i))
        return res