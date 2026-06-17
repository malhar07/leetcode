class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(ind, res):
            if len(res) == k:
                output.append(res.copy())
                return
            if ind>n:
                return
            res.append(ind)
            backtrack(ind+1, res)

            res.pop()
            backtrack(ind+1, res)
        backtrack(1,[])
        return output            