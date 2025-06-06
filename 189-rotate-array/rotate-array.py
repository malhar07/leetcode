class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        temp = nums[-k:]
        nums[-(len(nums)-k):] = nums[:len(nums)-k]
        nums[:k] = temp

