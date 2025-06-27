class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def dfs(prev,ind):
            if ind == len(costs):
                return 0
            if (prev,ind) not in memo:
                min_cost = math.inf
                for i, cost in enumerate(costs[ind]):
                    if i == prev:
                        continue
                    curr = cost + dfs(i, ind+1)
                    min_cost = min(min_cost, curr)
                memo[(prev,ind)] = min_cost
            return memo[(prev,ind)]
        
        return dfs(3,0)