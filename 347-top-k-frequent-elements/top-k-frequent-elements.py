class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_a ={}

        for i in nums:
            if i in dict_a :
                dict_a[i] +=1
            else:
                dict_a[i] = 1

        res=[] 
        arr = [[i[0], i[1]] for i in dict_a.items()]
        arr = sorted(arr, key = lambda x : x[1], reverse = True)
        print(arr)
        for i in range(k):
            res.append(arr[i][0])
            # maxx=0
            # key=-1
            # for j in dict_a.items():
            #     if j[1]>maxx:
            #         maxx=j[1]
            #         key = j[0]
            # res.append(key)
            # dict_a.pop(key)
        return res