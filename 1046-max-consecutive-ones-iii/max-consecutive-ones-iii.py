class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_z = 0
        left = 0
        right = 0
        res = 0
        curr_len = 0
        while right < len(nums):
            if nums[right] == 0 and curr_z == k:
                res = max((right-left), res)
                while left < right and nums[left] != 0:
                    left += 1
                left += 1
                curr_z -= 1
            else:
                if nums[right] == 0:
                    curr_z += 1
                right += 1
        return max(res, (right-left))