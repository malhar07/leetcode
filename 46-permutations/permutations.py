class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        def helper(p, up):
            #base case
            if len(up) == 0:
                # res.append(p)
                return [p]
            curr = []
            for i in range(len(p)+1):
                perm = p[0:i] + [up[0]] + p[i:]
                curr.extend(helper(perm, up[1:]))
            return curr
        
        return helper([], nums)


