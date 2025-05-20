class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        num_set = SortedList()

        for i in range(len(nums)):
            indx = num_set.bisect_left(nums[i])
            if indx != len(num_set) and num_set[indx] - nums[i] <= valueDiff:
                return True
            
            if indx > 0 and nums[i] - num_set[indx-1] <= valueDiff:
                return True
            
            num_set.add(nums[i])

            if len(num_set) > indexDiff:
                num_set.remove(nums[i-indexDiff])
        return False
                