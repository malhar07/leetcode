class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        word_map = defaultdict(list) # word -> synonyms
        word_groups = {} #word -> ID

        if len(sentence1)!=len(sentence2):
            return False

        for w1, w2 in similarPairs:
            word_map[w1].append(w2)
            word_map[w2].append(w1)

        def bfs(word,w_id):
            q = deque([word])

            while q:
                curr_word = q.popleft()

                if curr_word in word_groups:
                    continue
                for syn in word_map[curr_word]:
                    if syn not in word_groups:
                        q.append(syn)
                word_groups[curr_word] = w_id

        w_id = 0
        for word in word_map:
            if word not in word_groups:
                bfs(word, w_id)
                w_id += 1
        print(word_groups)
        for word1, word2 in zip(sentence1, sentence2):
            if word1!=word2 and (word1 not in word_groups or word2 not in word_groups or word_groups[word1] != word_groups[word2]):
                return False
                
        return True