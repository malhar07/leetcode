class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            
            if num-1 in num_set:
                continue
            else:
                num2 = num
                while num2+1 in num_set: 
                    num2 = num2+1
                res = max(res, num2-num+1)
        return res

        # num_set = set(nums)
        # res = 0

        # for i in range(len(nums)):
        #     num = nums[i]
        #     if num-1 in num_set:
        #         continue
        #     else:
        #         while num+1 in num_set:
        #             num += 1
        #         res = max(res, num+1-nums[i])
        # return res

