class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)

        for i in nums:
            arr[i-1] += 1
        res = [0, 0]
        for ind, i in enumerate(arr):
            if i == 2:
                res[0] = ind+1
            if i == 0:
                res[1] = ind+1
        return res