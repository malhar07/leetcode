from typing import List

class Trie:
    def __init__(self):
        self.children = {}  # string -> Trie
        self.end_of_folder = False

    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)

        res = []

        def dfs(node, path):
            if node.end_of_folder:
                res.append("/".join(path))
                return  # Do not go deeper once a folder is saved
            for name, child in node.children.items():
                dfs(child, path + [name])

        dfs(trie, [])
        return res
