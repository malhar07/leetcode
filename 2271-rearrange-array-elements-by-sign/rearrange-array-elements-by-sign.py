class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = 0
        # neg = 1

        # while pos < len(nums) and neg < len(nums):
        #     if nums[pos] < 0 and nums[neg] > 0:
        #         nums[pos], nums[neg] = nums[neg], nums[pos]
        #     # elif nums[pos] < 0 and nums[neg] < 0:
        #     #     nums[pos], nums[neg] = nums[neg], nums[pos]
        #     else:
        #         if nums[pos] > 0:
        #             pos += 2
        #         if nums[neg] < 0:
        #             neg += 2
        # return nums

        res = []
        pos = []
        neg = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res