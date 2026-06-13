class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)

        for num in nums:
            dict1[num] += 1
        for key, value in dict1.items():
            if value >= (len(nums)+1)//2:
                return key