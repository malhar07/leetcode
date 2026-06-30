class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        lowest = [math.inf, math.inf]
        for p in prices:
            if p <= lowest[0]:
                lowest[1] = lowest[0]
                lowest[0] = p
            elif p<lowest[1]:
                lowest[1] = p
        if lowest[0] + lowest[1] > money:
            return money
        return money - (lowest[0] + lowest[1])