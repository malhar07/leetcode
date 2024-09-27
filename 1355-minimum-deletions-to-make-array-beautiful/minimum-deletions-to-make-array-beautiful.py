class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deleted = 0
        ind = 0
        while ind < len(nums)-1:
            if nums[ind] == nums[ind+1]:
                deleted += 1
                ind+=1
            else:
                ind+=2
        return len(nums) - (((len(nums)-deleted)//2)*2)
        # if (len(nums)-deleted) % 2 == 0:
        #     return deleted
        # return deleted + 1