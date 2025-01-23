class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict1 = {}
        res = []
        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        for k,v in dict1.items():
            for ind in range(v):
                if ind == len(res):
                    res.append([k])
                else:
                    res[ind].append(k)
        return res
