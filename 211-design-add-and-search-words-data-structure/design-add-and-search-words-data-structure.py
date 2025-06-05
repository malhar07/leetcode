class Node:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(ind, curr):

            if len(word) ==ind:
                return curr.word
            c = word[ind]
            
            if c != ".":
                if c not in curr.children:
                    return False
                return dfs(ind + 1, curr.children[c])
            else:
                for child in curr.children:
                    found = dfs(ind+1, curr.children[child])
                    if found:
                        return True
                return False
            # return True
        return dfs(0,curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)