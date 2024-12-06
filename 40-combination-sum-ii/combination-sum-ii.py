class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(ind, subset, sum1):
            if sum1 == target:
                res.append(subset[:])
                return

            if ind>=len(candidates) or sum1>target:
                return 

            subset.append(candidates[ind])
            helper(ind+1, subset, sum1+candidates[ind])

            subset.pop()
            while ind+1<len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1
            helper(ind+1, subset, sum1)
        helper(0, [], 0)
        return res