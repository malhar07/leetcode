class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind-1]:
                nums[write] = nums[ind]
                write+=1
        return write