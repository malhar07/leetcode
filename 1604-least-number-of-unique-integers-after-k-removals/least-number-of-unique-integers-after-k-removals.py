class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        for i in arr:
            dict1[i] += 1
        count = 0
        for i in sorted(dict1.values()):
            if k >= i:
                count += 1
                k-=i
        return len(dict1) - count
