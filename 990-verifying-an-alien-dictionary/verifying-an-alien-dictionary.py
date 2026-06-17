class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for index, char in enumerate(order):
            order_dict[char] = index
        for i in range(1,len(words)):
            word1 = words[i-1]
            word2 = words[i]
            ind1, ind2 = 0,0

            while ind1 < len(word1):
                if ind2 >= len(word2):
                    return False
                if word1[ind1] == word2[ind2]:
                    ind1+=1
                    ind2+=1
                    continue
                if order_dict[word1[ind1]] > order_dict[word2[ind2]]:
                    return False
                break
        return True