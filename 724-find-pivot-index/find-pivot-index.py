class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]*len(nums)
        for i in range(1,len(nums)):
            left_sum.append(left_sum[i-1]+nums[i-1])
        write = len(nums)-2
        for i in range(len(nums)-1):
            right_sum[write] = right_sum[write+1]+nums[write+1]
            write-=1
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1