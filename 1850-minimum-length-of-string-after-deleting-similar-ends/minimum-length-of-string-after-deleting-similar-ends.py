class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                curr = s[left]
                while left < len(s) and s[left] == curr:
                    left += 1
                while right >= 0 and s[right] == curr:
                    right -= 1
            else:
                break
        return max(0, right-left+1)
                # return right-left+1