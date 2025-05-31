class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        visited = set()
        dist = 1
        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<len(rooms) and 0<=newc<len(rooms[0]) and (newr,newc) not in visited and rooms[newr][newc] not in [0,-1]:
                        rooms[newr][newc] = dist
                        q.append((newr,newc))
                        visited.add((newr,newc))
            dist+=1