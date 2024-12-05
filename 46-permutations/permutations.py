class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(res, nums):
            if len(nums) == 0:
                ans.append(res)
                return
            
            for i in range(len(res)+1):
                # temp = []
                print(i, " ", nums)
                temp = res[:i] + [nums[0]] + res[i:]
                helper(temp, nums[1:])
        helper([nums[0]], nums[1:])
        return ans