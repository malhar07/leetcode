class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        def bfs():
            visited = set()
            curr_distance = 1

            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()

                    for dr, dc in dirs:
                        newr, newc = r+dr, c+dc
                        if 0<=newr<len(rooms) and 0<=newc<len(rooms[0]) and rooms[newr][newc] > 0 and (newr,newc) not in visited:
                            rooms[newr][newc] = curr_distance
                            visited.add((newr,newc))
                            q.append((newr,newc))
                curr_distance += 1
        bfs()
        # return 