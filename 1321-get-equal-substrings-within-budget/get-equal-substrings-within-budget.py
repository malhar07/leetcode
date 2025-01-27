class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for i in range(len(s)):
            arr.append(abs(ord(s[i]) - ord(t[i])))
        left = 0
        cost = 0
        res = 0
        for right in range((len(arr))):
            cost += arr[right]

            while cost>maxCost:
                cost-=arr[left]
                left+=1
            res = max(res, right-left+1)
        return res