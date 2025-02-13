class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for i in spells:
            ind = -1
            count = 0
            left = 0
            right = len(potions)-1
            while left<=right:
                mid = (left+right)//2
                if potions[mid]*i >= success:
                    ind = mid
                    right = mid-1
                else:
                    left = mid+1
            if ind == -1:
                res.append(0)
            else:
                res.append(len(potions)-ind)
        return res
