class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = -1

        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                if int(num[i:i+3]) > val:
                    val = int(num[i:i+3])
                    res = num[i:i+3]
        return res