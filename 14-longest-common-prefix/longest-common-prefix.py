class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        # curr_char = strs[0][0]

        for ind, curr_char in enumerate(strs[0]):
            for word in strs:
                if ind>=len(word) or word[ind] != curr_char:
                    return prefix
            prefix+=curr_char
        return prefix