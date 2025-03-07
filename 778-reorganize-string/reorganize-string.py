class Solution:
    def reorganizeString(self, s: str) -> str:
        arr = []
        heap = []

        counts = Counter(s)
        print(counts)

        for key,val in counts.items():
            if val > (len(s)+1)//2:
                return ""
            heapq.heappush(heap,[-val, key])
        print(heap)
        while heap:
            if len(heap) >= 2:
                first = heapq.heappop(heap)
                second = heapq.heappop(heap)

                arr.append(first[1])
                arr.append(second[1])

                # first[0] += 1
                if first[0] != -1:
                    heapq.heappush(heap, [first[0]+1, first[1]])
                if second[0] != -1:
                    heapq.heappush(heap, [second[0]+1, second[1]])
            else:
                first = heapq.heappop(heap)
                if abs(first[0])>1:
                    return ""
                arr.append(first[1])
        print(arr)
        return "".join(arr)
                

        
            