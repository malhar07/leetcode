class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums[i], nums[write] = nums[write], nums[i]
                write-=1
        return write+1