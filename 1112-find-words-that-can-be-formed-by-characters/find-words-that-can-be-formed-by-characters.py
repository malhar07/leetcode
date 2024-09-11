class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = {}
        count = 0
        for i in chars:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1
        
        
        
        for w in words:
            temp = char_dict.copy()
            isValid = True
            for i in w:
                if i in temp:
                    if temp[i] == 0:
                        isValid = False
                        break
                    temp[i] -= 1
                else:
                    isValid = False
                    break
            if isValid:
                count += len(w)
            
        return count
            