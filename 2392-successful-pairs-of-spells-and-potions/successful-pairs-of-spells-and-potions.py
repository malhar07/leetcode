class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []

        potions.sort()

        for i in spells:
            target = success/i

            left = 0
            right = len(potions)-1

            while left <= right:
                mid = (left+right)//2
                if potions[mid] >= target:
                    right = mid-1
                elif potions[mid] < target:
                    left = mid+1
            if potions[mid] >= target:
                res.append(len(potions) - mid)
            else:
                res.append(len(potions) -mid-1)
        return res
