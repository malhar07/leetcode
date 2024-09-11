class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dict1 = {}

        for word in words:
            for letter in word:
                if letter in dict1:
                    dict1[letter] += 1
                else:
                    dict1[letter] = 1
        div = len(words)

        for i in dict1.values():
            if i%div != 0:
                return False
        return True