class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict1 = {nums[0]:0}
        # x = 0
        dict1 = {}
        for ind in range(len(nums)):
            x = target-nums[ind]
            if x in dict1:
                return [ind, dict1[x]]
            else:
                dict1[nums[ind]] = ind
    # comment