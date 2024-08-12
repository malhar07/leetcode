class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        max_avg = sum(nums[:k])/k
        for i in range(k):
            total+=nums[i]
        avg = total/k

        for i in range(k, len(nums)):
            total+= nums[i]-nums[i-k]
            avg = total/k
            if avg>max_avg:
                max_avg = avg
        return max_avg