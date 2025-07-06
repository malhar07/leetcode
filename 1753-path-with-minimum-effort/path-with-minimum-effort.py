class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = []
        heapq.heappush(min_heap,[0,0,0])
        visited = set()

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def bfs():

            while min_heap:
                effort, r,c = heapq.heappop(min_heap)
                if (r, c) in visited:
                    continue
                visited.add((r,c))
                if r == rows-1 and c == cols-1:
                    return effort
                for dr, dc in directions:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in visited:
                        max_effort = max(effort, abs(heights[r][c] - heights[newr][newc]))
                        heapq.heappush(min_heap, [max_effort,newr,newc])
                        
        return bfs()


