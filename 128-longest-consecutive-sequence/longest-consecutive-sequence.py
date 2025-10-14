class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        count = 0

        for num in numset:
            if num-1 not in numset:
                curr = num
                while curr in numset:
                    count += 1
                    curr += 1
                res = max(res, count)
                count = 0
        return res