class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_visited = set()
        a_visited = set()
        p_q = deque()
        a_q = deque()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        for r in range(len(heights)):
            p_visited.add((r,0))
            p_q.append((r,0))
            a_visited.add((r,len(heights[0])-1))
            a_q.append((r, len(heights[0])-1))

        for c in range(len(heights[0])):
            p_visited.add((0,c))
            p_q.append(((0,c)))
            a_q.append((len(heights)-1, c))
            a_visited.add((len(heights)-1, c))

        
        def bfs(q, ocean, visited):
            while q:
                r,c = q.popleft()
                ocean.add((r,c))

                for dr, dc in directions:
                    newr, newc = r+dr, c+dc

                    if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and (newr,newc) not in visited and heights[newr][newc]>=heights[r][c]:
                        visited.add((newr,newc))
                        q.append((newr,newc))
            return ocean

        pacific = bfs(p_q, set(), p_visited)
        atlantic = bfs(a_q, set(), a_visited)
        return list(pacific.intersection(atlantic))

