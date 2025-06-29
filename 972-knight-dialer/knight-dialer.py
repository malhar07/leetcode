class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            0:[6,4],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        memo = {}
        def dfs(num, length):
            if length == 1:
                return 1
            if (num, length) not in memo:
                
                res = 0
                for nei in moves[num]:
                    res += dfs(nei, length-1)
                memo[(num,length)] =  res
            return memo[(num,length)]
        ans = 0
        for i in range(10):
            ans+=dfs(i, n)
        return ans % MOD
