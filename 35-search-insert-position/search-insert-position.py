class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        [2,3,5,6]
        """
        res = -1
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res+1 if res >-1 else 0