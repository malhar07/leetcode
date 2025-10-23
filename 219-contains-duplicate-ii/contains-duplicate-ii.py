class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numset = set()
        for ind, num in enumerate(nums):
            if ind-k > 0:
                numset.remove(nums[ind-k-1])
            if nums[ind] in numset:
                return True
            else:
                numset.add(num)
        return False
