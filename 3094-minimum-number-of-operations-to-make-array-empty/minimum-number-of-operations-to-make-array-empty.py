class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict1 = {}
        res = 0
        for i in nums:
            dict1[i] = dict1.get(i, 0)+1
        for val in dict1.values():
            if val == 1:
                    return -1

            while val>0:  
                if val%3 == 0:
                    res += val//3
                    val = 0
                else:
                    val-=2
                    res+=1
        return res