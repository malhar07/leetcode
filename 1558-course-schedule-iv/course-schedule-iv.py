class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = {}

        for i in range(numCourses):
            adjlist[i] = set()
        
        for i, j in prerequisites:
            adjlist[i].add(j)
        

        def bfs(crs):
            q = deque()
            q.append(crs)
            path = set()

            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    for course in adjlist[curr]:
                        if course not in path:
                            path.add(course)
                            q.append(course)
                        # adjlist[curr].add(course)
            adjlist[crs].update(path)
        res = []
        for i in range(numCourses):
            bfs(i)

        for pre, crs in queries:
            if crs in adjlist[pre]:
                res.append(True)
            else:
                res.append(False)
        return res