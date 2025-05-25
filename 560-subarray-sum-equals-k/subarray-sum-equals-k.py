class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,3,7,5,4, -5, 11]
        # [1,4,11,16,20,15,26]
        # [0,1,4,11,16,20,15]
        prefix = defaultdict(int)
        count = 0

        prefix[0] += 1
        _sum = 0
        for i in nums:
            _sum+=i
            if _sum - k in prefix:
                count += prefix[_sum-k]
            prefix[_sum] += 1
        return count

        
        