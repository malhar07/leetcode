class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] < nums[0]:
                if target < nums[mid]:
                    right = mid-1
                else:
                    if target <= nums[-1]:
                        left = mid+1
                    else:
                        right = mid-1


            # elif nums[mid] >= nums[0]:
            else:
                if target > nums[mid]:
                    left = mid+1
                else:
                    if target >= nums[0]:
                        right = mid-1
                    else:
                        left = mid+1
            if nums[mid] == target:
                return mid

        
        return -1