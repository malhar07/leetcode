class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            print(i, " dcdcd" )
            if i>0 and nums[i] == nums[i-1]:
                continue
            # if nums[i]>target:
            #     break
            for j in range(i+1, len(nums)-2):
                t1 = (nums[i]+nums[j])
                # if t1>target:
                #     break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                print(nums[j])
                left = j + 1
                right = len(nums)-1
                while left < right:
                    if t1 + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < len(nums) and nums[left] == nums[left-1]:
                            left+=1
                        while right>=0 and nums[right] == nums[right+1]:
                            right -= 1
                    elif t1 + nums[left] + nums[right] > target:
                        right-=1
                    else:
                        left += 1
        return res
        