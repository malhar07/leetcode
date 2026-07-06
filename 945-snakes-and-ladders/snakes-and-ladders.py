class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        def getPos(num):
            row = (n-1) - ((num-1) // n)
            col = (num-1) % n

            if ((num-1)//n + 2) % 2 != 0:
                col = (n-1) - col
            return (row,col)
        
        def bfs():
            q = deque([1])
            visited.add(1)
            rolls = 1
            while q:

                for i in range(len(q)):
                    pos = q.popleft()

                    for die in range(1,7):
                        next_pos = pos+die
                        if next_pos > n**2:
                            continue
                        row, col = getPos(next_pos)
                        if board[row][col] != -1:
                            next_pos =  board[row][col]
                        if next_pos == n**2:
                            return rolls
                        if next_pos in visited:
                            continue
                        q.append(next_pos)
                        visited.add(next_pos)
                rolls += 1
            return -1
        return bfs()