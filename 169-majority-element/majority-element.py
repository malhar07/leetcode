# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         element = -1
#         for i in range(len(nums)):
#             if count == 0:
#                 element = nums[i]
#             if nums[i] == element:
#                 count+=1
#             else:
#                 count-=1
            
#         return element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = -1
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                # count+=1
            if nums[i] == element:
                count+=1
            else:
                count-=1
            
        return element