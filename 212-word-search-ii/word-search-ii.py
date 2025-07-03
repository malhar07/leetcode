# class Node:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
# class Trie:
#     def __init__(self):
#         self.root = Node()
    
#     def add_word(self, word):
#         curr = self.root

#         for char in word:
#             if char not in curr.children:
#                 curr.children[char] = Node()
#             curr = curr.children[char]
#         curr.isWord = True
    
#     def search(self, prefix):
#         curr = self.root

#         for char in prefix:
#             if char not in curr.children:
#                 return 0
#             curr = curr.children[char]
#         if curr.isWord:
#             return 2
#         return 1

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         rows, cols = len(board), len(board[0])
#         trie = Trie()
#         for word in words:
#             trie.add_word(word)
#         directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
#         path = set()
#         def dfs(r,c,w):
            
#             w += board[r][c]
#             curr_res = []
#             res = trie.search(w)
#             if res == 0:
#                 return []
#             else:
#                 path.add((r,c))
#                 if res == 2:
#                     curr_res.append(w)
#                 for dr, dc in directions:
#                     newr, newc = r+dr, c+dc

#                     if 0<=newr<rows and 0<=newc<cols and (newr,newc) not in path:
#                         curr_res.extend(dfs(newr, newc, w))
#                 path.remove((r,c))
#                 return curr_res
#         ans = []
#         for i in range(rows):
#             for j in range(cols):
#                 ans.extend(dfs(i,j,""))
#         return list(set(ans))

from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores full word instead of boolean

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.word = word  # mark end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        rows, cols = len(board), len(board[0])
        found = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                found.add(next_node.word)
                next_node.word = None  # avoid duplicate search

            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    dfs(nr, nc, next_node)
            visited[r][c] = False

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root)

        return list(found)
