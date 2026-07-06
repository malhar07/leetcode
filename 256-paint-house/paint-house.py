class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = {}
        def dfs(color, ind):
            red = blue = green = math.inf
            if ind >= n:
                return 0
            if (color, ind) in memo:
                return memo[(color, ind)]
            
            if color != 0:
                red = costs[ind][0] + dfs(0, ind+1)
            if color != 1:
                blue = costs[ind][1] + dfs(1, ind+1)
            if color != 2:
                green = costs[ind][2] + dfs(2, ind+1)
            if (color, ind) not in memo:
                memo[(color, ind)] = min(red, blue, green)
            return memo[(color, ind)]
        return dfs(-1, 0)