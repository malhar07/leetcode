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
        if not digits:
            return []
        comb = []
        res = []
        def dfs(ind):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return 
            for char in dict1[digits[ind]]:
                comb.append(char)
                dfs(ind+1)
                comb.pop()
        dfs(0)
        return res
            

