class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one = 0
        res = 0
        dict1 = {}
        for ind,num in enumerate(nums):
            if num == 1:
                one+=1
            else:
                one-=1
            if one == 0:
                res = ind+1
            
            if one not in dict1:
                dict1[one] = ind
            else:
                res = max(res, ind-dict1[one])
        return res