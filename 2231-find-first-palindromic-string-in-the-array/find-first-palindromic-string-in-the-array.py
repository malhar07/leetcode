class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(word):
            left = 0
            right = len(word)-1

            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        for word in words:
            if isPal(word):
                return word
        return ""


            