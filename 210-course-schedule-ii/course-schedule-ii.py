class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {}
        visited = set()

        path = {}
        pos = 0
        # loop = False
        for i in range(numCourses):
            adjlist[i] = []
        
        for crs, pre in prerequisites:
            adjlist[crs].append(pre)
        
        def dfs(crs):
            nonlocal pos
            if crs in visited:
                return False
            if crs in path:
                return True
            if adjlist[crs] == []:
                if crs not in path:
                    path[crs] = pos
                    pos+=1

                return True
            
            visited.add(crs)
            for n in adjlist[crs]:
                if not dfs(n):
                    return False
            # if crs not in path:
            path[crs] = pos
            pos+=1
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if crs not in path:
                if not dfs(crs):
                    return []
        res = [0]*numCourses
        for crs, ind in path.items():
            res[ind] = crs
        return res