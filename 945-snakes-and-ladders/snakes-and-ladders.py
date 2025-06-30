class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]
        for ind, row in enumerate(board):
            if ind%2 == 1:
                board[ind] = row[::-1][:]
        visited = set([0])
        q = deque([(0)])
        def bfs():
            turns = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr >= n**2-1:
                        return turns

                    for die in range(1,7):
                        new_pos = curr+die
                        # if new_pos not in visited:
                        # visited.add(new_pos)
                        r,c = new_pos//n, new_pos%n
                        if 0<=r<n and 0<=c<n and board[r][c]!=-1:
                            new_pos = board[r][c]-1
                        if new_pos not in visited:
                            q.append(new_pos)
                            visited.add(new_pos)
                turns+=1
            return -1    
        return bfs()
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]
        for i, row in enumerate(board):
            if i % 2 == 1:
                board[i] = row[::-1][:]

        visited = set([0])
        q = deque([0])

        def bfs():
            turns = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == n * n - 1:
                        return turns

                    for die in range(1, 7):
                        new_pos = curr + die
                        if new_pos >= n * n:
                            continue
                        r, c = new_pos // n, new_pos % n
                        if board[r][c] != -1:
                            new_pos = board[r][c] - 1

                        if new_pos not in visited:
                            visited.add(new_pos)
                            q.append(new_pos)
                turns += 1
            return -1

        return bfs()
