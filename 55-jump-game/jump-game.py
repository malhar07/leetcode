# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True
        # right = len(nums)-1
        # left = len(nums)-2

        # while left >= 0:
        #     if left + nums[left] >= right:
        #         right -= 1
        #     left-=1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=goal-(i):
                goal=i
        return goal==0
        
