class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(num, subset):

            if len(subset) == k:
                res.append(subset)
                return

            if num > n :
                return 
            helper(num+1, subset[:])
            subset.append(num)
            helper(num+1, subset[:])
        helper(1, [])
        return res