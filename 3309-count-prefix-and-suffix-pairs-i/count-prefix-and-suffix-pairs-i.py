class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def helper(s1, s2):
            return s1.startswith(s2) and s1.endswith(s2)
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                count+=helper(words[j], words[i])
        return count