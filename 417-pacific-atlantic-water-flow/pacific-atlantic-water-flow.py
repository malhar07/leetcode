class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        dp = {}

        def bfs(r1,c1):
            q = deque([(r1,c1)])
            flows = [False, False]
            visited = set([(r1,c1)])

            while q:
                r,c = q.popleft()
                # print(r," ",c)
                if r==0 or c == 0:
                    flows[0] = True
                if r == len(heights)-1 or c == len(heights[0])-1:
                    flows[1] = True
                if flows[0] == True and flows[1] == True:
                    dp[(r1,c1)] = True
                    return True
                

                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc
                    # if (newr,newc) in dp :
                    #     if dp[(newr,newc)] == False:
                    #         continue
                    #     else:
                    #         dp[(r1,c1)] = True
                    #         return True

                    if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and heights[newr][newc] <= heights[r][c] and (newr,newc) not in visited:
                        q.append((newr,newc))
                        visited.add((newr, newc))
            dp[(r1,c1)] = False
            return False
        
        res = []
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if bfs(i,j):
                    res.append([i,j])
        return res
                