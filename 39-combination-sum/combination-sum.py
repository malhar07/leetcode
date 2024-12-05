class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(ind, subset, sum1):
            if target == sum1:
                res.append(subset[:])
                return

            if ind >= len(candidates) or sum1>target:
                return 
            
            helper(ind+1, subset[:], sum1)

            subset.append(candidates[ind])
            helper(ind, subset[:], sum1+candidates[ind])
            # subset.pop()
        helper(0, [], 0)
        return res