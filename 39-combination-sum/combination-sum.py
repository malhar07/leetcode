class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        nums = candidates
        def helper(ind, sum1):
            
            if sum1 == target:
                res.append(subset[:])
                return
            
            if ind>=len(nums) or sum1 > target:
                return
            
            subset.append(nums[ind])
            sum1+=nums[ind]
            helper(ind, sum1)

            sum1-=subset.pop()
            helper(ind+1, sum1)

        helper(0,0)
        return res