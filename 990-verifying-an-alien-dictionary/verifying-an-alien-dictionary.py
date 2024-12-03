class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordr = {}
        ind=1
        for i in order:
            ordr[i] = ind
            ind+=1
        print (ordr)
        def compare(word1, word2):
            ind1 = 0
            ind2 = 0
            while ind1<len(word1) and ind2 <len(word2):
                # if word1[ind1] == word2[ind2]:
                #     continue
                if ordr[word1[ind2]] < ordr[word2[ind2]]:
                    return True
                elif ordr[word1[ind2]] > ordr[word2[ind2]]:
                    return False
                ind1+=1
                ind2+=1
            if ind2 == len(word2) and ind1 == len(word1):
                return True
            if ind2 == len(word2):
                return False
            return True

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                print(words[1], " ", words[j])
                if not compare(words[i], words[j]):
                    return False
        return True