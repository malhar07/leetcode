class Solution:
    def reverse(self, x: int) -> int:
        neg = True
        if x>0:
            neg = False
        else:
            x = x*-1
        ans = 0

        while x > 0:
            digit = x%10
            if ((2**31-1) - ans*10) < digit:
                return 0
            ans = ans*10 + digit
            x=x//10
        if neg:
            return ans*-1
        return ans