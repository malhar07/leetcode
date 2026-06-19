class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)
        res = []
        visited = set()
        processed = set()
        def dfs(crs):
            if crs in visited:
                return False

            visited.add(crs)
            
            for nei in premap[crs]:
                if nei in processed:
                    continue
                if not dfs(nei):
                    return False
            if crs not in processed:
                res.append(crs)
                processed.add(crs)
            visited.remove(crs)

            return True
        
        for crs in range(numCourses):
            if crs not in processed:
                if not dfs(crs):
                    return []
        return res            