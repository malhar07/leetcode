# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         directions = [[0,1], [0,-1], [1,0], [-1,0]]
#         path = set()

#         def dfs(row, col):
#             self.gold += grid[row][col]
            
#             if self.max_gold == 0:
#                 self.max_gold = self.gold
#             else:
#                 self.max_gold = max(self.max_gold, self.gold)
            

#             path.add((row,col))
#             for r, c in directions:
#                 newr, newc = row+r, col+c
#                 if 0<=newr<m and 0<=newc<n and grid[newr][newc] != 0 and (newr, newc) not in path:
#                     path.add((newr, newc))
#                     dfs(newr, newc)
#             self.gold -= grid[row][col]
#             path.remove((row, col))

#             return self.max_gold




#         res = 0
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] != 0:
#                     self.gold = 0
#                     self.max_gold = 0
#                     res = max(res, dfs(row, col))
#         return res


# from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col, path, gold_collected):
            # Collect gold at the current cell
            gold_collected += grid[row][col]
            path.add((row, col))  # Mark the cell as visited

            # Initialize max_gold to current collected gold
            max_gold = gold_collected

            # Explore all possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < m and
                    0 <= new_col < n and
                    grid[new_row][new_col] > 0 and
                    (new_row, new_col) not in path
                ):
                    max_gold = max(max_gold, dfs(new_row, new_col, path, gold_collected))

            # Backtrack: unmark the cell as visited
            path.remove((row, col))
            return max_gold

        # Main logic: iterate over all cells to find the maximum gold
        max_gold_overall = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] > 0:  # Start DFS only on gold cells
                    max_gold_overall = max(max_gold_overall, dfs(row, col, set(), 0))

        return max_gold_overall
