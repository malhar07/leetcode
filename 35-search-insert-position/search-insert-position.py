class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # start = 0
        # end = len(nums)-1
        # while(start<=end):
        #     mid = int((start+end)/2)
        #     if nums[mid] == target:
        #         return mid
        #     else:
        #         if nums[mid]>target:
        #             end = mid-1
        #         else:
        #             start = mid+1
        # if nums[mid]<target:

        #     return mid+1
        # else:
        #     return mid


        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if target < nums[mid]:
            return mid
        return mid+1