class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[-1]

        for ind in range(len(nums)-2):
            left = ind+1
            right = len(nums)-1

            curr_sum = nums[ind]+nums[left]+nums[right]
            # if abs(curr_sum-target) < abs(res-target):
            #     res = curr_sum
            while left < right:
                curr_sum = nums[ind]+nums[left]+nums[right]
                if abs(curr_sum-target) < abs(res-target):
                    res = curr_sum
                if curr_sum == target:
                    return target
                elif curr_sum<target:
                    left+=1
                else:
                    right-=1
        return res
                    


            