class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        res = []
        for word in strs:
            if str(sorted(word)) in dict1:
                dict1[str(sorted(word))].append(word)
            else:
                dict1[str(sorted(word))] = [word]
        for key, val in dict1.items():
            res.append(val)
        return res
            