class Solution:
    def alienOrder(self, words: List[str]) -> str:
        next_char = defaultdict(list)
        unique_chars = set()
        for word in words:
            for char in word:
                unique_chars.add(char)
        for ind in range(1,len(words)):
            pos = 0
            while pos < len(words[ind-1]) and pos < len(words[ind]) and words[ind-1][pos] == words[ind][pos]:
                pos+=1
            if pos >= len(words[ind]):
                if pos < len(words[ind-1]):
                    return ""
                
            if pos < len(words[ind-1]) and pos < len(words[ind]):
                next_char[words[ind-1][pos]].append(words[ind][pos])
        res = []
        visited = set()
        path = set()

        def dfs(char):
            if char in path:
                return False
            if char in visited:
                return True
            
            visited.add(char)
            path.add(char)
            
            for _next in next_char[char]:
                if not dfs(_next):
                    return False
            path.remove(char)
            res.append(char)
            return True

            
        
        for char in unique_chars:
            if not dfs(char):
                return ""
        return "".join(res[::-1])