from bisect import bisect_left, bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit))
        memo = {}
        
        def backtrack(ind):
            if ind == len(arr):
                return 0
            
            if ind in memo:
                return memo[ind]

            
            j = bisect_right(arr, (arr[ind][1],-1,-1 ))

            res = arr[ind][2] + backtrack(j)

            res = max(res, backtrack(ind+1))
            memo[ind] = res

            return res
        return backtrack(0)