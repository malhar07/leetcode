class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()

        q = deque()
        q.append(x)
        q.append(y)
        visited.add(x)
        visited.add(y)

        water = [x, y, -x, -y]

        while q:
            curr = q.popleft()

            if curr == target:
                return True
            
            for w in water:
                if curr+w >= 0 and curr+w <= (x+y) and curr+w not in visited:
                    q.append(curr+w)
                    visited.add(curr+w)
        return False
            