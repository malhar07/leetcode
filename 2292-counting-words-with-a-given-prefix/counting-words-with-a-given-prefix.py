class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            count+= word.startswith(pref)
            # found = True
            # for ind, char in enumerate(pref):
            #     if ind>= len(word) or word[ind]!=char:
            #         found = False
            #         break
            # if found:
            #     count+=1
        return count