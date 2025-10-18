class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos_count = 0
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] <= 0:
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
            else:
                left += 1
        if nums[right]<=0:
            pos_count = right

        else:
            pos_count = right+1
        # print(nums[i])

        for i in range(pos_count):
            print(nums[i])

            if abs(nums[i]) <= pos_count:
                
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        if pos_count<1:
            return 1

        for i in range(pos_count):
            if nums[i]>0:
                return i+1
        return pos_count+1

        [2,3,1,5,-1,-3]