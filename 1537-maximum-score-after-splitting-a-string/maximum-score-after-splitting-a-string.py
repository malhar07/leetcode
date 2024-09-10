class Solution:
    def maxScore(self, s: str) -> int:
        ones,zeroes = 0,0
        res = 0
        for i in s:
            if i == "1":
                ones+=1
            else:
                zeroes += 1
        curr_ones = 0
        for i in range(0, len(s)-1):
            if s[i] == "1":
                curr_ones +=1
            res = max(res, ones + i+1 - 2*curr_ones)
        return res