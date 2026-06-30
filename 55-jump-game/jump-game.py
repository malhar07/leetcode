class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # reachable = set(len(nums)-1)
        pos = len(nums)-1
        target = len(nums)-1
        for i in range(len(nums)-2,-1,-1):

            curr_jump = nums[i]
            curr_index = i

            if curr_index + curr_jump >= target:
                target = curr_index
        return target == 0


