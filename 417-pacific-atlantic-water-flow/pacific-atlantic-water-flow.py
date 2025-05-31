class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        pacific = deque()
        atlantic = deque()

        def bfs(que):
            visited = set()
            res = set()

            while que:
                r,c = que.popleft()
                res.add((r,c))
                visited.add((r,c))

                for dr,dc in dirs:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and heights[newr][newc] >= heights[r][c] and (newr,newc) not in visited:
                        que.append((newr,newc))
                        visited.add((newr,newc))
            return res

        for i in range(len(heights)):
            pacific.append((i,0))
            atlantic.append((i, len(heights[0])-1))
        for i in range(len(heights[0])):
            pacific.append((0,i))
            atlantic.append((len(heights)-1, i))

        
        pacific = bfs(pacific)
        atlantic = bfs(atlantic)

        return list(atlantic & pacific)
        