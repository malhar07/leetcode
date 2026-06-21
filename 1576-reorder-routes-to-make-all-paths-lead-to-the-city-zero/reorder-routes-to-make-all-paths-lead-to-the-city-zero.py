class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        routes = set()
        adjlist = defaultdict(list)
        res = 0
        visited = set()
        visited.add(0)

        for c1, c2 in connections:
            routes.add((c1,c2))
            adjlist[c1].append(c2)
            adjlist[c2].append(c1)

        q = deque([0])

        while q:
            city = q.popleft()

            for nei in adjlist[city]:
                if nei in visited:
                    continue
                if (nei,city) not in routes:
                    res += 1
                q.append(nei)
                visited.add(nei)
        return res