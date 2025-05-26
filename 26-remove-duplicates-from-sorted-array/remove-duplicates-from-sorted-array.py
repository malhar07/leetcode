class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        indx = 0
        while indx<len(nums):
            if indx == len(nums)-1 or nums[indx] != nums[indx+1]:
                nums[write] = nums[indx]
                write+=1
            indx+=1
        return write