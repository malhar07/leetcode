class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = 0
        nums2 = set(nums)
        for num in nums2:
            if num-1 not in nums2:
                count = 1
                while num+1 in nums2:
                    count += 1
                    num+=1
            res = max(res,count)
        return res
