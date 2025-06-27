class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel_set = set(jewels)
        for stone in stones:
            if stone in jewel_set:
                count+=1
        return count