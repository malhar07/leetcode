class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        arr = sorted(items, key = lambda x: x[0])

        max_beauty = 0
        dict1 = {} #dictionary to store the mapping of price an beauty
        prices = [] # array to store prices

        #populate the ditionary and prices array

        for ind, i in enumerate(arr):
            if i[1] > max_beauty:
                max_beauty = i[1]
            if ind == len(arr)-1 or arr[ind][0] != arr[ind+1][0]:
                dict1[i[0]] = max_beauty
                prices.append(i[0])
        print(dict1)
        print(prices)

        def binary(arr, target):
            left= 0
            right = len(arr)-1

            while left <= right:
                
                mid = (left+right)//2
                print(mid)
                if arr[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            if mid == 0 and arr[mid] > target:
                return -1
            else:
                # return mid
                if arr[mid] < target:
                    return mid
                else:
                    return mid-1

        ans = []
        for q in queries:
            if q in dict1:
                ans.append(dict1[q])
            else:
                ind = binary(prices, q)
                if ind == -1:
                    ans.append(0)
                else:
                    ans.append(dict1[prices[ind]])
        return ans
            




'''
sort the items array
[[1,2], [2,4], [3,2], [3,5], [5,6],]
{
    1:2
    2:4
    3:5
    5:6
}
[1,2,3,5]
[1,2,3,4,5,6]

[0,1,2,3,5,6]
'''