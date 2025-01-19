class Solution:
    def frequencySort(self, s: str) -> str:
        # dict1 = {}
        # for i in s:
        #     dict1[i] = dict1.get(i,0)+1
        # arr = []
        # for k,v in dict1.items():
        #     arr.append((v,k))
        # arr.sort(reverse = True)

        # ans = ""
        # for count, char in arr:
        #     ans+=char*count
        # return ans

        char_count = {}
        count_map = {}
        res = ""
        for i in s:
            char_count[i] = char_count.get(i,0)+1
        for k,v in char_count.items():
            if v in count_map:
                count_map[v].append(k)
            else:
                count_map[v] = [k]
        for i in range(len(s), 0,-1):
            if i in count_map:
                for char in count_map[i]:
                    res+=char*i
        return res