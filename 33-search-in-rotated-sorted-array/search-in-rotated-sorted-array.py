class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                #left half
                if nums[mid] < target:
                    left = mid+1
                else:
                    if target >= nums[0]:
                        right = mid-1
                    else:
                        left = mid+1
            else:
                # right half
                if nums[mid] > target:
                    right = mid-1
                else:
                    if target >= nums[0]:
                        right = mid-1
                    else:
                        left = mid+1
        return -1