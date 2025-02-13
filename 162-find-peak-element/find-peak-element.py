class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        while left <= right:
            mid = (left+right)//2
            if mid-1 < 0 or nums[mid-1] < nums[mid]:
                if mid+1 == len(nums) or nums[mid+1] <nums[mid]:
                    return mid
                else:
                    left = mid+1
            else:
                right = mid-1
        return mid