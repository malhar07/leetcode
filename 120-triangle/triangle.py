class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = {}
        def helper(level, ind):
            if level == n:
                return 0
            if (level,ind) in dp:
                return dp[(level,ind)]
            left = helper(level+1, ind)
            right = helper(level+1, ind+1)
            dp[(level,ind)] = min(left,right) + triangle[level][ind]

            return min(left,right) + triangle[level][ind]
            
            # _sum += triangle[level][ind]

            # return min(left,right)
        return helper(0,0)