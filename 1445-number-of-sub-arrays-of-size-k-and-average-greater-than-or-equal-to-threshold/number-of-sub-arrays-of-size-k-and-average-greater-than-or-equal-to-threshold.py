class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        average = 0
        for i in range(k-1):
            average += arr[i]
        for i in range(k-1, len(arr)):
            average += arr[i]
            if average / k >= threshold:
                res += 1
            average-=arr[i-(k-1)]
        return res
