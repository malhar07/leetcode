class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # subset = []

        def helper(ind,subset):
            if ind>= len(nums):
                res.append(subset[:])
                return
            
            helper(ind+1, subset[:])

            subset.append(nums[ind])
            helper(ind+1, subset[:])

            # subset.pop()
        helper(0, [])

        return res
