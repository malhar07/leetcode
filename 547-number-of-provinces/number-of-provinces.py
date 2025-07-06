class UnionFind:
    def __init__(self, n):
        # self.parent = {i:i for i in range(n)}
        # self.rank = {i:0 for i in range(n)}
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
        else:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        res = set()
        for node in range(len(isConnected)):
            res.add(uf.find(node))
        return len(res)
