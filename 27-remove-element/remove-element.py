class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        ind = 0 
        while ind < len(nums):
            if nums[ind] != val:
                nums[ind], nums[write] = nums[write], nums[ind]
                write +=1
            ind+=1
        return write