class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        res = 0
        curr = 0

        char = defaultdict(int)

        while right < len(s):
            char[s[right]] +=1
            curr = max(curr, char[s[right]])

            if (right-left+1) - curr > k:
                res = max(res, right-left)
                char[s[left]] -= 1
                left+=1
            right += 1
            # else:
        return max(res, right-left)

