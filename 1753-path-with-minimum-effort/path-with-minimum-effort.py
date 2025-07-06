class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = []
        visited = set()
        heapq.heappush(min_heap,[0,0,0]) #[effort,r,c]

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if r == rows-1 and c == cols-1:
                return effort

            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr, dc in directions:
                newr, newc = r+dr, c+dc
                if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in visited:
                    new_effort = max(effort, abs(heights[r][c] - heights[newr][newc]))
                    heapq.heappush(min_heap, [new_effort, newr, newc])
                
