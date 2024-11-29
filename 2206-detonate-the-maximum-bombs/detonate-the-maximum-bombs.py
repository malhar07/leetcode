class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dist(x1,y1,x2,y2):
            return ((x1-x2)**2 + (y1-y2)**2)**0.5
        adjlist = {}
        for i in range(len(bombs)):
            adjlist[i] = []
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i==j:
                    continue
                if dist(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]:
                    adjlist[i].append(j)
        

        def bfs(i):
            count = 1
            q = deque()
            q.append(i)
            path = set()
            path.add(i)

            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    for neigh in adjlist[curr]:
                        if neigh not in path:
                            q.append(neigh)
                            path.add(neigh)
                            count+=1
            return count

        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i))
        return res
            