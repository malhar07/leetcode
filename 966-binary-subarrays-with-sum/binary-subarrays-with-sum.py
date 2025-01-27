class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict1 = defaultdict(int)
        dict1[0]+=1
        pre = 0
        total = 0
        for i in nums:
            pre+=i
            total += dict1[pre-goal]
            dict1[pre]+=1
        return total

