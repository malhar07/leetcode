class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        cnt = Counter(nums)

        def helper(perm, cnt):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in cnt:
                if cnt[i] >0:
                    perm.append(i)
                    cnt[i] -= 1
                    helper(perm, cnt)
                    perm.pop()
                    cnt[i]+=1
                
        helper([], cnt)
        return res