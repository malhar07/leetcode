class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def charDiff(word1, word2):
            if len(word1) != len(word2):
                return False
            count = 0
            for i in range(len(word1)):

                if word1[i] != word2[i]:
                    count+=1
                if count >= 2:
                    return False
            return True
        adjlist = defaultdict(list)
        temp = wordList+[beginWord]
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if charDiff(temp[i],temp[j]):
                    adjlist[temp[i]].append(temp[j])
                    adjlist[temp[j]].append(temp[i])
        visited = set()
        visited.add(beginWord)
        def bfs():
            q = deque([(beginWord,0)])
            # length = -1
            while q:
                word, length = q.popleft()
                if word == endWord:
                    return length+1
                for nei in adjlist[word]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,length+1))
            return 0
        return bfs()
        
