class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        res = -1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                if nums[mid] > nums[0]:
                    left = mid+1
                else:
                    if target >nums[right]:
                        right = mid-1
                    else:
                        left = mid+1
            else:
                if nums[mid] < nums[0]:
                    right = mid-1
                else:
                    if target>=nums[left]:
                        right = mid-1
                    else:
                        left = mid+1
        return res