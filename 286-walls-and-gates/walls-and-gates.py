class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row, col = len(rooms), len(rooms[0])
        visited = set()
        q = deque()
        dist = 0

        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    visited.add((r, c))
                    q.append((r,c))

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist

                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    newr = r+dr
                    newc = c+dc
                    if newr <0 or newr>=len(rooms) or newc < 0 or newc>=len(rooms[0]) or rooms[newr][newc] == -1 or (newr,newc) in visited:
                        continue
                    visited.add((newr,newc))
                    q.append((newr,newc))
            dist+=1
                
