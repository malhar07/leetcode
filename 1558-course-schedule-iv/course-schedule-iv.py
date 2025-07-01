class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = defaultdict(set)
        for pre, crs in prerequisites:
            prereq[crs].add(pre)
        visited = [False] * numCourses

        def dfs(crs):
            if visited[crs]:
                return prereq[crs]
            visited[crs] = True
            new_set = set()
            for pre in prereq[crs]:
                new_set.update(dfs(pre))
            prereq[crs].update(new_set)
            return prereq[crs]

        for crs in range(numCourses):
            dfs(crs)
        res = []
        for pre, crs in queries:
            if pre in  prereq[crs]:
                res.append(True)
            else:
                res.append(False)
        return res