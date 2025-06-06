class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num>=10:
            while num>0:
                total+=num%10
                num = num//10
            num = total
            total = 0
        return num