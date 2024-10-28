class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = -1
        dict1 = {}

        for i in nums:
            dict1[i] = 1
        
        for i in nums:
            count = 1
            curr = i
            while curr**2 in dict1:
                curr = curr**2
                count+=1
            if count >=2 and count> res:
                res = count
        return res
                