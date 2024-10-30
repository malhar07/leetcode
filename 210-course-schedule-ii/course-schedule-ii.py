class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {}
        visited = set()

        path = []
        # loop = False
        for i in range(numCourses):
            adjlist[i] = []
        
        for crs, pre in prerequisites:
            adjlist[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if adjlist[crs] == []:
                if crs not in path:
                    path.append(crs)
                return True
            
            visited.add(crs)
            for n in adjlist[crs]:
                if not dfs(n):
                    return False
            if crs not in path:
                path.append(crs)
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return path