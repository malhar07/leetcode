class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        tribo = [0,1,1]
        for i in range(3,n+1):
            curr = sum(tribo)
            tribo[0], tribo[1] = tribo[1], tribo[2]
            tribo[2] = curr
        return tribo[2]