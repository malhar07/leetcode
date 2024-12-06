class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []

        def helper(ind, subset):
            if ind>= len(nums):
                res.append(subset[:])
                return 
            helper(ind+1, subset)
            subset.append(nums[ind])
            helper(ind+1, subset)
            subset.pop()
        helper(0,[])
        ans = 0
        print(res)
        for arr in res:
            xor = 0
            for ele in arr:
                xor^=ele
            ans+=xor
        return ans