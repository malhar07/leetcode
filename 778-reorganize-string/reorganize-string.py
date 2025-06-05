class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        heap = []
        maxCount = 0
        for c in s:
            counter[c]+=1
            maxCount = max(maxCount,counter[c])
        if maxCount*2 > len(s)+1:
            return ""
        for k,v in counter.items():
            heapq.heappush(heap,(-v,k))
        res = []
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            res.append(char1)
            res.append(char2)
            count1 += 1
            count2+=1
            if count1 != 0:
                heapq.heappush(heap,(count1,char1))
            if count2 != 0:
                heapq.heappush(heap,(count2,char2))
        if heap:
            res.append(heap[0][1])
        return "".join(res)