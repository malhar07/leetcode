class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,-1,0,1,2,4]
        res = []
        nums.sort()

        for ind, num in enumerate(nums):
            if ind>0 and nums[ind] == nums[ind-1]:
                continue
            left = ind + 1
            right = len(nums)-1
            while left < right:
                if nums[ind] + nums[left] + nums[right] == 0:
                    res.append([nums[ind], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left+=1
                    while right>=0 and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[ind] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left += 1
        return res
