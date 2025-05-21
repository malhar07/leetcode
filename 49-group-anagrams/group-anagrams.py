class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        result = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
        # print(word_dict)
        for val in word_dict.values():
            result.append(val)
        # print(result)
        return result