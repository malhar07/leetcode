class Solution:
    def fib(self, n: int) -> int:
        if n ==0:
            return 0
        if n == 1:
            return 1
        fib1 = 0
        fib2 = 1
        ind = 2
        while ind <= n:
            res = fib1 + fib2
            fib1 = fib2
            fib2 = res
            ind+=1

        return res