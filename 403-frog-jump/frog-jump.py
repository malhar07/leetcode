class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stonedict = {val : ind for ind, val in enumerate(stones)}
        memo = {}
        def backtrack(jump, index):
            if (jump, index) in memo:
                return memo[(jump,index)]

            if index == len(stones)-1:
                return True
            # if jump<=0:
            #     return False
            for i in range(jump-1, jump+2):
                if i == 0:
                    continue
                stone = stones[index]+i
                if stone in stonedict:
                    if backtrack(i, stonedict[stone]):
                        memo[(jump, index)] = True
                        return True
            memo[(jump,index)] = False
            return False
        return backtrack(0,0)