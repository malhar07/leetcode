"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_graph = {}

        for emp in employees:
            emp_graph[emp.id] = emp
        
        res = 0

        def dfs(emp):
            imp = 0
            imp += emp.importance

            for sub in emp.subordinates:
                imp += dfs(emp_graph[sub])
            return imp
        return dfs(emp_graph[id])
