class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(start, subset):

            if len(subset) == k:
                res.append(subset[:])
                return

            for i in range(start, n+1):
                subset.append(i)
                helper(i+1, subset)
                subset.pop()

            # if num > n :
            #     return 

            # helper(num+1, subset[:])

            # subset.append(num)
            # helper(num+1, subset[:])
        helper(1, [])
        return res