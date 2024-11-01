class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        visited = set()
        path = set()

        for i in range(numCourses):
            adjlist[i] = []
        for crs, pre in prerequisites:
            adjlist[crs].append(pre)
        
        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
            
            path.add(crs)
            
            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False
            visited.add(crs)
            path.remove(crs)

            return True
                




        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True