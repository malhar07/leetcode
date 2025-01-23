class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dict1 = defaultdict(int)
        curr = 0
        res = 0
        for i in range(len(s)):
            dict1[s[i]] += 1
            curr = max(curr, dict1[s[i]])

            if ((i+1) - left) - curr <= k:
                res = i+1 - left
            else:
                
                dict1[s[left]] -= 1
                left+=1
        return res
