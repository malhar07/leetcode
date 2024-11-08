class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = set()
        non_terminal = set()
        # self.cycle = False

        def dfs(node):
            if graph[node] == [] or node in terminal:
                terminal.add(node)
                return True

            if node in loop or node in non_terminal:
                print(node)
                return False
            
            loop.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            terminal.add(node)
            loop.remove(node)
            return True

        res = []
        for i in range(len(graph)):
            if i in terminal or i in non_terminal:
                continue
            loop = set()
            if dfs(i):
                terminal.add(i)
                # for j in loop:
                #     terminal.add(j)
            else:
                for j in loop:
                    non_terminal.add(j)
        terminal = sorted(list(terminal))
        return terminal