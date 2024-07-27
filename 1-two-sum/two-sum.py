class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {nums[0]:0}
        x = 0
        for ind in range(1,len(nums)):
            x = target-nums[ind]
            if x in dict1:
                return [ind, dict1[x]]
            else:
                dict1[nums[ind]] = ind
    # comment