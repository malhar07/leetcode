class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rows, cols = len(rooms), len(rooms[0])
        q = deque()


        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        

        def bfs(q):
            steps = 0

            while q:
                
                # visited.add((r,c))

                for i in range(len(q)):
                    r,c = q.popleft()
                    rooms[r][c] = steps
                    for dr, dc in directions:
                        newr, newc = r+dr, c+dc

                        if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in visited and rooms[newr][newc]  == 2147483647:
                            q.append((newr,newc))
                            visited.add((newr,newc))
                steps += 1
        bfs(q)
