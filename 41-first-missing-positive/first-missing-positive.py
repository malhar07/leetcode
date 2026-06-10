class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one = False
        for i in range(len(nums)):
            if nums[i] == 1:
                one = True
            if nums[i] <= 0:
                nums[i] = 1
        if not one:
            return 1
        for ind, num in enumerate(nums):
            index = abs(num)
            if index <= len(nums) and index!=0:
                if nums[index-1]>0:
                    nums[index-1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
