class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def helper(sub, nums):
            if len(nums)==0:
                if len(sub)>0:
                    return 1
                return 0
            add_1 = 0
            if nums[0]-k not in sub:
                sub.append(nums[0])
                add_1 = helper(sub, nums[1:])
                sub.pop()
            add_0 = helper(sub, nums[1:])
            return add_1+add_0


        return helper([], nums)