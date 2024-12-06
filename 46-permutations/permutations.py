class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(p, up):
            #base case
            if len(up) == 0:
                res.append(p)
                return 
            for i in range(len(p)+1):
                perm = p[0:i] + [up[0]] + p[i:]
                helper(perm, up[1:])
        helper([], nums)
        return res


