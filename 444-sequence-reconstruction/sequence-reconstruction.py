class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        adjlist = {i:set() for i in range(1, len(nums)+1)}

        for sub in sequences:
            if len(sub)>1:
                for ind in range(len(sub)-1):
                    adjlist[sub[ind]].add(sub[ind+1])

        for node, ele_set in adjlist.items():
            indegree[node] += 0
            for element in ele_set:
                indegree[element] += 1
        
        q = deque()
        for ele, indeg in indegree.items():
            if indeg == 0:
                q.append(ele)
        print(indegree)
        print(adjlist)
        
        res = []
        while q:
            print(q)
            if len(q) > 1:
                return False
            curr = q.popleft()
            res.append(curr)
            for nei in adjlist[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(res)
        if len(res) == len(nums):
            return True
        return False