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
        temp = node
        if not node:
            return None

        start = Node(temp.val)
        map1 = {1:start}
        
        visited = set()

        q = deque()
        q.append((start, temp))
        while q:
            curr, tmp = q.popleft()
            # print(curr.val)

            for nei in tmp.neighbors:
                if (tmp.val, nei.val) not in visited:

                    visited.add((tmp.val, nei.val))
                    if nei.val in map1:
                        node = map1[nei.val]
                    else:
                        node = Node(nei.val)
                        map1[nei.val] = node

                    curr.neighbors.append(node)
                    q.append((node, nei))
        return start
