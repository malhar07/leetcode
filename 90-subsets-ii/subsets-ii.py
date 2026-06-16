class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(ind, arr):
            if ind >= len(nums):
                res.append(arr.copy())
                return
                            
            arr.append(nums[ind])
            backtrack(ind+1, arr)

            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1
            
            arr.pop()
            backtrack(ind+1, arr)
        backtrack(0, [])
        return res
