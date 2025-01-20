class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # if len(nums) < 3:
        #     return -1
        perimeter = 0 #nums[0]+nums[1]
        ans = -1

        for i in range(0, len(nums)):
            if nums[i] < perimeter:
                print(nums[i], perimeter)
                ans = perimeter+nums[i]
            perimeter +=nums[i]
        return ans
            