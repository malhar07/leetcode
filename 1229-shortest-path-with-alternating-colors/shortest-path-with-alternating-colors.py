class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n

        adjlist_red = defaultdict(list)
        adjlist_blue = defaultdict(list)

        for edge in redEdges:
            adjlist_red[edge[0]].append(edge[1])
        for edge in blueEdges:
            adjlist_blue[edge[0]].append(edge[1])

        visited = set()

        q = deque()
        q.append([0,0,None])
        visited.add((0,None))

        while q:
            node, dist, col = q.popleft()

            if res[node] == -1:
                res[node] = dist

            if col != "BLUE":
                for nei in adjlist_blue[node]:
                    if (nei,"BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        q.append([nei, dist+1, "BLUE"])
            if col != "RED":
                for nei in adjlist_red[node]:
                    if (nei,"RED") not in visited:
                        visited.add((nei,"RED"))
                        q.append([nei, dist+1, "RED"])

        return res
