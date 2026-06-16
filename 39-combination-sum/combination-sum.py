class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(ind, total, res):
            if total == target:
                output.append(res.copy())
                return
            if ind >= len(candidates) or total>target:
                return

            #1 Take the candidate
            res.append(candidates[ind])
            backtrack(ind, total+candidates[ind], res)

            res.pop()
            backtrack(ind+1, total, res)
        backtrack(0, 0, [])
        return output