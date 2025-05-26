class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
# [-4,-1,-1,0,1,2]
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while right<left and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left += 1
        return res