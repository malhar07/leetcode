class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = 0
        tank = 0
        g = 0
        # if sum(gas) < sum(cost):
        #     return -1
        # else:
        for i in range(len(gas)):
            g += gas[i]-cost[i]
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                curr = i+1
                tank=0
        if g < 0:
            return -1
        return curr
        return curr if curr<len(gas) else -1


        
