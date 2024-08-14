class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in range(len(gain)):
            res.append(gain[i]+res[i])  
        return max(res)    