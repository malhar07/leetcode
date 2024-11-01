# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         board = board[::-1]
#         self.res = len(board)*len(board[0])
#         for row in range(len(board)):
#             if row%2 == 1:
#                 board[row] = board[row][::-1]
#         visited = set()
        
#         def dfs(square, flag):
#             row, col = (square-1)//6, (square-1)%6

#             q = deque()
#             q.append(square)
#             visited.add(square)
#             moves = 0

#             while q:
#                 for i in range(len(q)):
#                     square = q.popleft()
#                     if square == len(board)*len(board[0]):
#                         return moves
#                     if board[(square-1)//6][(square-1)%6] != -1:
#                         q.append(board[(square-1)//6][(square-1)%6])
#                         # flag = False
#                         continue

#                     for j in range(1,7):
#                         if square+j <= len(board)*len(board[0]) and square+j not in visited:
#                             q.append(square+j)
#                             visited.add(square+j)
#                 moves+=1
#             return -1
#         return dfs(1, False)
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Flip and prepare the board for easier indexing
        n = len(board)
        board = board[::-1]
        for i in range(n):
            if i % 2 == 1:
                board[i] = board[i][::-1]

        def get_coordinates(square):
            """Convert square number to board coordinates."""
            r, c = (square - 1) // n, (square - 1) % n
            return r, c
        
        visited = set()
        q = deque([(1, 0)])  # Start from square 1 with 0 moves
        
        while q:
            square, moves = q.popleft()

            if square == n * n:  # If reached the last square
                return moves

            # Try moving from square by rolling the die (1 to 6 steps)
            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    break
                
                r, c = get_coordinates(next_square)
                
                # If there's a ladder or snake, move to the target square
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))

        # If the last square is unreachable
        return -1
