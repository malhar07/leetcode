class Trie:
    def __init__(self):
        self.children = {}
        self.wordCount = 0

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()

            curr = curr.children[char]
            curr.wordCount += 1

    def search(self, prefix):
        curr = self

        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.wordCount
        # def dfs(curr):
        #     count = 0

        #     for child in curr.children.values():
        #         count += dfs(child)
        #     return count + curr.wordCount
        # return dfs(curr)
                
                
    
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.search(pref)
