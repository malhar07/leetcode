class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return 
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        if self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for v1, v2 in edges:
            if uf.find(v1) == uf.find(v2):
                return [v1, v2]
            uf.union(v1,v2)