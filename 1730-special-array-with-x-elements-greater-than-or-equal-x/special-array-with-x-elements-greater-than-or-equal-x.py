class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = len(nums)
        nums.sort()
        if nums[0] >= count:
            return count
        else:
            count-=1

        for ind in range(1, len(nums)):
            if nums[ind] >= count:
                if nums[ind-1] < count:
                    return count
            count-=1
        return -1