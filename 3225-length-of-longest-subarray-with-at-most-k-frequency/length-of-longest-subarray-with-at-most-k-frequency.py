class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        left = 0
        res = 0
        for ind, i in enumerate(nums):
            dict1[i] += 1
            # print(dict1[i])
            if dict1[i] >k:
                while dict1[i] != k:
                    dict1[nums[left]] -= 1
                    left+=1
            # else:
            print(ind, " ", left)
            res = max(res, ind-left+1)
        return res
                