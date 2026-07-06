class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        con = set()
        adjlist = defaultdict(list)
        res = 0
        visited = set()

        for n1, n2 in connections:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

            con.add((n1,n2))
        
        q = deque([(0,-1)]) #curr, parent
        visited.add(0)

        while q:
            curr, parent = q.popleft()

            for nei in adjlist[curr]:
                if nei == parent:
                    continue
                if (curr,nei) in con:
                    res+=1
                visited.add(nei)
                q.append((nei, curr))
        return res
                
