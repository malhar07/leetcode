class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = 0
        res = []
        for i in range(0,len(nums)):
            if i==0 or nums[i] == nums[i-1]+1:
                length +=1
            else:
                length = 1

            if length >= k:
                res.append(nums[i])
            else:
                res.append(-1)
        return res[k-1:]
           
            
             
