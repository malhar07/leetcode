class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # def pre(num1, num2):
        #     num1 = str(num1)
        #     num2 = str(num2)
        #     length = min(len(str(num1)), len(str(num2)))
        #     count = 0

        #     for i in range(length):
        #         if num1[i] == num2[i]:
        #             count+=1
        #         else:
        #             break
        #     return count
        # print(len(arr1), " ", len(arr2))
        
        # res = 0
        # for i in arr1:
        #     for j in arr2:

        #         res = max(res, pre(i, j))
        # return res

        dict1 = defaultdict(int)
        for i in arr1:
            prefix = ""
            for j in str(i):
                prefix += j
                dict1[prefix] += 1
        res = 0
        

        for i in arr2:
            prefix = ""
            for j in str(i):
                prefix += j
                if dict1[prefix] > 0:
                    print(prefix)
                    res = max(res, len(prefix))
        return res