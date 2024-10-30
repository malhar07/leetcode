class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        visited = set()

        for i in range(numCourses):
            adjlist[i] = []


        for crs, pre in prerequisites:
            adjlist[crs].append(pre)

        def dfs(i):
            if i in visited:
                return False
            if adjlist[i] == []:
                return True
            visited.add(i)
            for neighbor in adjlist[i]:
                if not dfs(neighbor):
                    return False
                adjlist[i].remove(neighbor)
            visited.remove(i)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            