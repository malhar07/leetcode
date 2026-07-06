class Solution:
    def tribonacci(self, n: int) -> int:
        one = 0
        two = 1
        three = 1

        if n==0:
            return 0
        if n<=2:
            return 1
        for i in range(3,n+1):
            curr = one+two+three
            
            
            one = two
            two = three
            three = curr
        return curr