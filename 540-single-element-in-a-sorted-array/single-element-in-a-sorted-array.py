class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        if len(nums) == 1:
            return nums[0]


        while left <= right:
            mid = (left+right)//2
            if mid == len(nums)-1 or (nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]):
                return nums[mid]
            else:
                if (len(nums) - mid - 1) % 2 == 0:
                    if nums[mid+1] != nums[mid]:
                        right = mid-1
                    else:
                        left = mid+1

                else:
                    if nums[mid+1] != nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1


