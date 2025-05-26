class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        for ind in range(len(nums)-2):
            if target>0 and nums[ind] > target:
                break
            # if ind>0 and nums[ind] == nums[ind-1]:
            #     continue
            
            left = ind+1
            right = len(nums)-1
            while left<right:
                print(left, " ", right)
                if nums[ind] + nums[left] + nums[right] < target:
                    # res.append([nums[ind], nums[left], nums[right]])
                    res+=right-left
                    # while left > right and nums[left] == nums[left+1]:
                    #     left+=1
                    # while right< left and nums[right] == nums[right-1]:
                    #     right-=1
                    left+=1
                elif nums[ind] + nums[left] + nums[right] >= target:
                    right-=1
        return res