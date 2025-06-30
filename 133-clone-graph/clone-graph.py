"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        visited = set()
        if not node:
            return None

        def bfs(node):
            visited.add(node)
            q = deque([node])
            node_map[node] = Node(node.val)

            while q:
                curr = q.popleft()

                for nei in curr.neighbors:
                    if nei not in visited:
                        node_map[nei] = Node(nei.val)
                        q.append(nei)
                        visited.add(nei)
                    node_map[curr].neighbors.append(node_map[nei])
        bfs(node)
        return node_map[node]
                

