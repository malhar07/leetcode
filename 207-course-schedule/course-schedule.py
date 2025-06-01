class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for a,b in prerequisites:
            adjlist[a].append(b)
        visited = set()
        seen = set()

        def dfs(crs):
            if crs not in adjlist:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            seen.add(crs)
            
            for nei in adjlist[crs]:

                if not dfs(nei):
                    return False
            del adjlist[crs]
            visited.remove(crs)
            return True


        for i in range(numCourses):
            if i not in seen:
                if not dfs(i):
                    return False
        return True