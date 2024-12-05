class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        for i in range(len(nums)):
            start = 0
            if i>0 and nums[i] == nums[i-1]:
                start = end+1
            end = len(res)-1 
            
            for j in range(start, len(res)):
                temp = res[j].copy()
                temp.append(nums[i])
                res.append(temp)    
                   
        return res
