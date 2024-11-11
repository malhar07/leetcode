class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        res = []
        for i in nums1:
            dict1[i]+=1
        for i in nums2:
            if dict1[i] > 0:
                res.append(i)
                dict1[i]-=1
        return res