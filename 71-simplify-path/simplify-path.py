class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        res = []

        for folder in stack:
            if folder == "." or folder == "":
                continue
            elif folder == '..':
                if res:
                    res.pop()
            else:
                res.append(folder)
        return "/"+"/".join(res)