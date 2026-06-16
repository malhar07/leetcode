class Solution:
    def reorganizeString(self, s: str) -> str:
        arr = Counter(s)

        arr = [[-val, key] for key, val in arr.items()]
        res = ""

        heapq.heapify(arr)
        if abs(arr[0][0]) > (len(s)+1)//2:
            return ""

        while len(arr) > 1:

            count1, char1 = heapq.heappop(arr)
            count2, char2 = heapq.heappop(arr)

            res += char1 + char2
            count1 += 1
            count2 += 1

            if count1 < 0:
                heapq.heappush(arr,[count1, char1])
            if count2 < 0:
                heapq.heappush(arr, [count2, char2])
        if arr:
            if abs(arr[0][0]) > 1:
                return ""
            else:
                return res+arr[0][1]
        return res
        
