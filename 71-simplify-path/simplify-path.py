class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        for i in s:
            if i == "..":
                if stack:
                    stack.pop()
                continue
            if i != "." and i != "":
                stack.append(i)
        res = ""
        print(stack)
        for i in stack:
            res += "/" + i
        if res == "":
            return "/"
        return res