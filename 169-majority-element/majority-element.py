class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        n = len(nums)//2

        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        
        for i in nums:
            if dict1[i] > n:
                return i