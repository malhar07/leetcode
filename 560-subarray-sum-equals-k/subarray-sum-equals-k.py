class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ind_map = defaultdict(int)
        ind_map[0] = 1
        res = 0
        curr_sum = 0
        for num in nums:
            curr_sum+=num
            if curr_sum-k in ind_map:
                res += ind_map[curr_sum-k]
            ind_map[curr_sum] += 1
        return res