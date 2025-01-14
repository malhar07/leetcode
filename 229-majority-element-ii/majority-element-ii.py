class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        res = []
        n = len(nums)//3

        for i in nums:
            dict1[i] = dict1.get(i, 0)+1
        for i in nums:
            if dict1[i] > n:
                res.append(i)
        return list(set(res))