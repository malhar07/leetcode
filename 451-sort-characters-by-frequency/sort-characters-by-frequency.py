class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i,0)+1
        arr = []
        for k,v in dict1.items():
            arr.append((v,k))
        arr.sort(reverse = True)

        ans = ""
        for count, char in arr:
            ans+=char*count
        return ans