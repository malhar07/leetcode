class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = copy.deepcopy(nums)
        arr.sort()

        left = 0
        right = len(nums)-1

        while left < len(nums) and nums[left] == arr[left]:
            left+=1
        if left == len(nums):
            return 0
        while right >= 0 and nums[right] == arr[right]:
            right-=1
        # if left == 
        return right-left+1