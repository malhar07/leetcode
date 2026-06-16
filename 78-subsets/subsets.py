class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ind, arr):
            if ind >= len(nums):
                res.append(arr.copy())
                return


            arr.append(nums[ind])
            backtrack(ind+1, arr)

            arr.pop()
            backtrack(ind+1, arr)
        backtrack(0, [])
        return res            