class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0
    
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
            curr.count += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        for word in words:
            root.add_word(word)
        
        def traverseTrieTree(root, word):
            total_sum = 0

            for char in word:
                root = root.children[char]
                total_sum += root.count
            return total_sum
        
        res = []
        for word in words:
            res.append(traverseTrieTree(root, word))
        return res