class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-2
        mid = 0

        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1

        while left <= right:
            mid = (left+right)//2
            print(mid)

            if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                left = mid+1
            elif nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid]:
                left = mid+1
            elif nums[mid-1] > nums[mid] and nums[mid+1] < nums[mid]:
                right = mid-1
            else:
                return mid
        return mid
            