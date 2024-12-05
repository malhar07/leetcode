class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        res = []

        def helper(num):
            if len(subset) == k:
                res.append(subset[:])
                return 

            if num > n:
                return

            subset.append(num)
            helper(num+1)

            subset.pop()
            helper(num+1)
        helper(1)
        return res