class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for ind, i in enumerate(s):
            # print(i, " ",int(i)%2)
            if int(i) != ind%2:
                count += 1
        return min(count, len(s)-count)