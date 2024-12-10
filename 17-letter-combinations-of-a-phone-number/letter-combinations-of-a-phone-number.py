class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",""
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if len(digits) == 0:
            return []
        res = []
        # print(dict1[digits[0]])
        def helper(ind, s):

            if ind >= len(digits):
                res.append(s)
                return

            for char in dict1[digits[ind]]:
                print(char)
                s += char
                helper(ind+1, s)
                s = s[:-1]
        helper(0, "")
        return res



