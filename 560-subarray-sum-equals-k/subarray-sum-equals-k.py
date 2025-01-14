class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        dict1 = {}
        presum = 0
        for i in nums:
            presum += i
            if presum == k:
                count+=1

            
            if presum-k in dict1:
                count+= dict1[presum-k]
            dict1[presum] = dict1.get(presum,0)+1
            
        return count
        # [1,4,-2,2,5,-1,]
        # [1,5, 3,5,10, 9]