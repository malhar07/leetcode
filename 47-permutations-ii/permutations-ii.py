class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(arr, used):
            
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            # if ind >= len(nums):
            #     return 
            visited = set()
            for i in range(len(nums)):
                if not used[i] and nums[i] not in visited:
                    used[i] = True
                    visited.add(nums[i])
                    arr.append(nums[i])
                    helper(arr, used)
                    arr.pop()
                    used[i] = False
                else:
                    continue
        
        helper([],[False]*len(nums))
        return res
            
        