class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        def helper(ind, curr):
            nonlocal max_len
            if ind>=len(arr):
                max_len = max(max_len, len(curr))
                return

            temp = curr[:]
            for char in arr[ind]:
                if char in temp:
                    helper(ind+1, curr)
                    return
                else:
                    temp+=char
            curr += arr[ind]
            helper(ind+1, curr)
            curr = curr[:-len(arr[ind])]
            helper(ind+1, curr)
        
        helper(0, "")
        return max_len