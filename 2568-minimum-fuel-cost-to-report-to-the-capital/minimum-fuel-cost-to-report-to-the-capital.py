class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        total_length = len(roads)+1
        res = 0

        neighbors = defaultdict(list)
        visited = set()

        for c1, c2 in roads:
            neighbors[c1].append(c2)
            neighbors[c2].append(c1)
        print(neighbors)

        def dfs(node):
            nonlocal res
            visited.add(node)
            curr_number_of_nodes = 1
            for nei in neighbors[node]:
                if nei not in visited:
                    curr_number_of_nodes += dfs(nei)
            if node!=0:
                res+=math.ceil(curr_number_of_nodes/seats)
            return curr_number_of_nodes
        dfs(0)
        return res

