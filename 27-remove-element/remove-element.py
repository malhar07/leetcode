class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_ind = len(nums)-1
        ind = 0
        while ind<=swap_ind:
            if nums[ind] == val:
                nums[ind], nums[swap_ind] = nums[swap_ind], nums[ind]
                swap_ind -= 1
            else:
                ind+=1
        return swap_ind+1