class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        tot = m+n
        res = 1

        for i in range(m):
            
            res*=tot
            tot-=1
            print(res)
        while m > 0:
            res //= m
            m-=1
        return int(res)