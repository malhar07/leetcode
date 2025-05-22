class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_a ={}

        for i in nums:
            if i in dict_a :
                dict_a[i] +=1
            else:
                dict_a[i] = 1

        res=[] 
        arr = [[] for _ in range(len(nums))]
        # print(dict_a)

        for key, val in dict_a.items():
            # print(key, " ", val)
            arr[val-1].append(key)

        for i in range(len(arr)-1,-1,-1):
            
            
            res.extend(arr[i])
            if len(res) == k:
                return res
            print(res)
        # arr = [[i[0], i[1]] for i in dict_a.items()]
        # arr = sorted(arr, key = lambda x : x[1], reverse = True)
        # # print(arr)
        # for i in range(k):
        #     res.append(arr[i][0])
        # return res