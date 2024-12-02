class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        def get_parent(node):
            while node != parent[node]:
                node = parent[node]
                parent[node] = parent[parent[node]]  # Path compression
                
            return node


        for x,y in edges:
            parent_x = get_parent(x)
            parent_y = get_parent(y)
            print(parent_x," ",parent_y)
            if parent_x == parent_y:
                return [x,y]
            if rank[parent_x] >= rank[parent_y]:
                parent[parent_y] = parent_x
                rank[parent_x] += rank[parent_y]
            else:
                parent[parent_x] = parent_y
                rank[parent_y] += rank[parent_x]
            
            
            
            
