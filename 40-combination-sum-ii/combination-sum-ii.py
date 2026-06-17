class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(ind,arr, total):
            
            if total == target:
                res.append(arr.copy())
                return
            
            if ind >= len(candidates) or total > target:
                return
                
            arr.append(candidates[ind])

            backtrack(ind+1, arr, total+arr[-1])
            
            arr.pop()

            while ind+1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1
            
            backtrack(ind+1, arr, total)
        backtrack(0, [], 0)

        return res