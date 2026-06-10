class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for ind, i in enumerate(nums):
            if ind>0 and nums[ind] == nums[ind-1]:
                continue
            target = i*-1

            left = ind+1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[ind], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left +=1
                    while right>left and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return res