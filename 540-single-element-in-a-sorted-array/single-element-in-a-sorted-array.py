class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # even and last then return
        left = 0
        right = len(nums)-1
        res = 0
        while left <= right:
            mid = (left+right)//2

            if mid%2 == 0:
                if mid == right:
                    return nums[mid]
                if nums[mid] != nums[mid+1]:
                    res = mid
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] != nums[mid-1]:
                    res = mid
                    right = mid-1
                else:
                    left = mid+1
        return nums[res]
