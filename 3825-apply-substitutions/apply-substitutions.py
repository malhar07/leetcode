class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replace = {"_":"_"}
        for key,val in replacements:
            replace[key] = val
        visited = set()
        def dfs(key,val):
            if key in visited:
                return val
            
            s = ""
            ind = 0
            while ind < len(val):
                if val[ind] == "%":
                    s+=dfs(val[ind+1],replace[val[ind+1]])
                    ind+=2
                else:
                    s+=val[ind]
                ind+=1
            replace[key] = s
            visited.add(key)
            return s
        for key,val in replace.items():
            if key not in visited:
                replace[key] = dfs(key,val)
        stack = []
        for char in text:
            if char!="%":
                stack.append(replace[char])
        return "".join(stack)