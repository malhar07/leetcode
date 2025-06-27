class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [False]*len(days)
        def helper(ind):
            if ind >= len(days):
                return 0
            if not memo[ind]:
                i = ind
                min_cost = math.inf
                for duration, cost in zip([1,7,30], costs):
                    validity = days[ind] + duration 
                    while i<len(days) and days[i] < validity:
                        i+=1
                    min_cost = min(min_cost, cost+helper(i))
                memo[ind] = min_cost
            return memo[ind]
        return helper(0)

