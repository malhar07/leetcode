class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = [-1] * len(nums)

        # def dfs(ind):
        #     if ind>=n:
        #         return 0
        #     if memo[ind] != -1:
        #         return memo[ind]
        #     rob_curr = nums[ind] + dfs(ind+2)
        #     skip = dfs(ind+1)
        #     if memo[ind] == -1:
        #         memo[ind] = max(skip, rob_curr)
        #     return memo[ind]
        # return dfs(0)




        # memo = [0] * (len(nums) + 2)


        # for i in range(len(nums)-1,-1,-1):
        #     curr = max((nums[i] + memo[i+2]), memo[i+1])
        #     memo[i] = curr
        # return memo[0]

        memo = [0,0]
        for i in range(len(nums)-1,-1,-1):
            curr = max((nums[i] + memo[1]), memo[0])
            memo[1] = memo[0]
            memo[0] = curr
        return memo[0]
