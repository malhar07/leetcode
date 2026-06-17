class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(ind, arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for i in range(len(arr)+1):
                backtrack(ind+1, arr[:i]+[nums[ind]]+arr[i:])
        backtrack(0,[])
        return res






#                         [1,2]
#     [3,1,2]             [1,3,2]             [1,2,3]
#   [:i]+[3]+[i+:]