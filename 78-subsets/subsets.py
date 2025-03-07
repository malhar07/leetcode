class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        # self.nums = nums
        def helper(arr, ind):
            if ind >= len(nums):
                res.append(arr[:])
                return
            arr.append(nums[ind])
            # ind+=1
            helper(arr,ind+1)
            arr.pop()
            helper(arr,ind+1)
        helper([],0)
        return res
            
        # res = []
        # # subset = []

        # def helper(ind,subset):
        #     if ind>= len(nums):
        #         # res.append(subset[:])
        #         return [subset[:]]
            
        #     left = helper(ind+1, subset[:])

        #     subset.append(nums[ind])
        #     right = helper(ind+1, subset[:])
        #     # subset.pop(). Pop is not used beacuse a copy of subset is passed on to the each recursive call
        #                     # (subset[:]) if a copy of subset is passed then the last element needs to be popped out.
        #     return left+right
        # return helper(0, [])

        # # return res
