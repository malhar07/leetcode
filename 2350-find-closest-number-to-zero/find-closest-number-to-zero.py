class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums:
            if abs(num) < abs(res) or (abs(num) == abs(res) and num>res):
                res = num
        return res