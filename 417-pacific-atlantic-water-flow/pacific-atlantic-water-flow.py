class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = set()
        def bfs(r,c):
            # print((r,c))
            pacific = False
            atlantic = False
            visited = set()
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    
                    if r == 0 or c == 0:
                        pacific = True
                    if c == len(heights[0])-1 or r == len(heights)-1:
                        atlantic = True
                    if (r,c) in res or (pacific and atlantic):
                        return True
                    
                    for dr, dc in directions:
                        if 0<= r+dr < len(heights) and 0<= c+dc < len(heights[0]) and (r+dr, c+dc) not in visited and heights[r][c] >= heights[r+dr][c+dc]:
                            q.append((r+dr, c+dc))
                            visited.add((r+dr, c+dc))
            return False 



        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if bfs(row, col):
                    res.add((row,col))
        return list(res)