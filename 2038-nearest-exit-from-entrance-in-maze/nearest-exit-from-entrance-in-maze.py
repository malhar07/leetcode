class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()

        def bfs(r,c,moves):
            q = deque()
            q.append((r,c, moves))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                for i in range(len(q)):
                    r,c,moves = q.popleft()
                    print((r,c), " ",(entrance[0], entrance[1]))
                    if (r == 0 or r== len(maze)-1 or c == 0 or c == len(maze[0])-1) and (r,c) != (entrance[0], entrance[1]):
                        return moves
            

                    for dr, dc in directions:
                        if 0<= r+dr < len(maze) and 0<=c+dc<len(maze[0]) and maze[r+dr][c+dc] == '.' and (r+dr, c+dc) not in visited:
                            q.append((r+dr, c+dc, moves+1))
                            visited.add((r+dr, c+dc))
            return -1
                
        return bfs(entrance[0], entrance[1], 0)

[["+",".","+","+","+","+","+"],
["+",".","+",".",".",".","+"],
["+",".","+",".","+",".","+"],
["+",".",".",".","+",".","+"],
["+","+","+","+","+","+","."]]