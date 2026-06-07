class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            for ind, char in enumerate(prefix):
                if ind < len(strs[i]):
                    if char != strs[i][ind]:
                        prefix = prefix[:ind]
                        break

                else:
                    prefix = prefix[:ind]
                    break
        return prefix