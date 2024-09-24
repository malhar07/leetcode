class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = 0
        right = 0
        total = 0

        curr_max = 0
        while right < len(colors):
            curr_max = neededTime[right]
            while right < len(colors) and colors[right] == colors[left]:
                curr_max = max(curr_max, neededTime[right])
                right += 1
            total += curr_max
            left = right
        return sum(neededTime) - total
            
            
