class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prereq[crs] == []:
                return True
            
            visited.add(crs)

            for nei in prereq[crs]:
                if not dfs(nei):
                    return False

            visited.remove(crs)

            prereq[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        










        0-1
        1-2
        2-4
        4-5