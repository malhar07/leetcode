class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1 = {}
        res = []
        for i in nums:
            if dict1.get(i,0) == 1:
                res.append(i)
            dict1[i] = dict1.get(i,0)+1
        return res