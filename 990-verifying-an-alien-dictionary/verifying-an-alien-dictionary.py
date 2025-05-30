class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_dict = {}
        for i in range(len(order)):
            alpha_dict[order[i]] = i
        
        def compare(char1, char2):
            print(char1)
            if alpha_dict[char1] <= alpha_dict[char2]:
                return True
            return False
        
        for i in range(1,len(words)):
            ind = 0
            while ind< len(words[i]) and ind < len(words[i-1]) and words[i][ind] == words[i-1][ind]:
                ind+=1
            if ind< len(words[i]) and ind < len(words[i-1]):
                char1 = words[i-1][ind]
                char2 = words[i][ind]
                if not compare(char1, char2):
                    return False
            if ind == len(words[i]) and ind<len(words[i-1]):
                return False
        return True