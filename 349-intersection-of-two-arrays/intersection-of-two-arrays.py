class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        res = []
        for i in nums1:
            dict1[i] += 1
        for i in nums2:
            if i in dict1:
                res.append(i)
        return set(res)