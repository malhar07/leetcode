class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        dict1[0] += 1
        res = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            res += dict1[curr_sum - k]

            dict1[curr_sum] += 1
        return res