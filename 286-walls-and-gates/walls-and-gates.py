class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        q= deque([])
        def bfs(q):
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            dist = 1
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        newr, newc = r+dr, c+dc

                        if 0<=newr<len(rooms) and 0<=newc<len(rooms[0]) and rooms[newr][newc] not in [0,-1] and (newr,newc) not in visited:
                            rooms[newr][newc] = dist#min(dist, rooms[newr][newc])
                            q.append((newr,newc))
                            visited.add((newr,newc))
                dist+=1

        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        bfs(q)