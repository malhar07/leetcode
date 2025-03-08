class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = [ i for i in range(1,n+1)]
        res = []
        def helper(arr, ind):
            if ind > n:
                if len(arr) == k:
                    res.append(arr[:])
                return
            
            arr.append(ind)
            helper(arr,ind+1)
            arr.pop()
            helper(arr, ind+1)
        helper([],1)
        return res


        # nums = [ i for i in range(1,n+1)]
        # res = []
        # def helper(arr, ind):
        #     if ind == len(nums):
        #         if len(arr) == k:
        #             res.append(arr[:])
        #         return
            
        #     arr.append(nums[ind])
        #     helper(arr,ind+1)
        #     arr.pop()
        #     helper(arr, ind+1)
        # helper([],0)
        # return res