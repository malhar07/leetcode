class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        res = 0

        for n1, n2 in connections:
            adjlist[n1].append((n2,1))
            adjlist[n2].append((n1,0))

        q = deque([(0,-1)]) #curr, parent

        while q:
            curr, parent = q.popleft()

            for nei, cost in adjlist[curr]:
                if nei == parent:
                    continue
                res+=cost
                q.append((nei, curr))
        return res