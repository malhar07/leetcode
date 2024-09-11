class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in tickets:
            count += min(i, tickets[k])
        for i in range(k+1, len(tickets)):
            if tickets[i] >= tickets[k]:
                count-=1
        return count