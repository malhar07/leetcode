class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(arr, _sum, ind):
            if ind == len(candidates):
                return 
            if _sum == target:
                print(arr)
                res.append(arr[:])
                return
            
            if _sum > target:
                return 
            
            arr.append(candidates[ind])
            _sum += candidates[ind]
            helper(arr, _sum, ind)

            temp=arr.pop()
            _sum-=temp
            
            helper(arr, _sum, ind+1)
        helper([], 0, 0)
        return res