class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        print(count)
        max_heap = []

        for word,freq in count.items():
            heapq.heappush(max_heap,(-freq,word))
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res

