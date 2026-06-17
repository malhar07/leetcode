class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(ind, arr):
            print(arr)
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            start = 0

            # If current number is a duplicate,
            # insert it only after its existing copy.
            if ind > 0 and nums[ind] == nums[ind - 1]:
                last_index = -1

                for i in range(len(arr)):
                    if arr[i] == nums[ind]:
                        last_index = i

                start = last_index + 1

            for i in range(start, len(arr)+1):
                backtrack(ind+1, arr[:i] + [nums[ind]] + arr[i:])

        backtrack(0,[])
        return res


[1,1,2,2]
    #     [1,2]
    # [2,1,2] [1,2,2]

