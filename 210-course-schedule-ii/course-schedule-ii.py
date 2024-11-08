class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        res = []

        adjlist = {}
        for i in range(numCourses):
            adjlist[i] = []
        for crs, pre in prerequisites:
            adjlist[crs].append(pre)

        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True

            visited.add(crs)
            path.add(crs)

            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False
            res.append(crs)
            path.remove(crs)  
            return True     
        for crs in range(numCourses):
            if crs not in visited:
                if not dfs(crs):
                    return []
        return res