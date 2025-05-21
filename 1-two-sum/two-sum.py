class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for ind, num in enumerate(nums):
            if target-num in num_dict:
                return [ind, num_dict[target-num]]
            num_dict[num] = ind