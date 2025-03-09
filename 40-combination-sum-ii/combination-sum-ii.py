class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(arr,ind):
            if sum(arr) == target:
                res.append(arr[:])
                return
            if sum(arr) > target:
                # res.append(arr[:])
                return
            if ind >= len(candidates):
                return
            
            arr.append(candidates[ind])
            helper(arr,ind+1)
            arr.pop()
            while ind<len(candidates)-1 and candidates[ind] == candidates[ind+1]:
                ind+=1
            
            helper(arr,ind+1)
            


        helper([],0)
        return res