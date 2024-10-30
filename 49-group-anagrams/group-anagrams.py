class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # dict1 = {}

        # for word in strs:
        #     w = str(sorted(word))
        #     if w in dict1:
        #         lst = dict1[w]
        #         lst.append(word)
        #         dict1[w] = lst #dict1[tuple(arr)].append(word)
        #     else:
        #         dict1[w] = [word]
        # print(dict1)
        # # for i in dict1.values():
        # #     # print(i)
        # #     ans.append(i)
        # res = dict1.values()
        # return res

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
            