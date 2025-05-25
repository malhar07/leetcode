class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        # post = [1]*len(nums)

        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        product_from_right = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            curr_num = nums[i]
            res[i] = res[i]*product_from_right
            product_from_right = product_from_right*curr_num
        return res
        