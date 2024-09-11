class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for i in s:
            dict1[i] += 1
        for ind in range(len(s)):
            if dict1[s[ind]] == 1:
                return ind
        return -1