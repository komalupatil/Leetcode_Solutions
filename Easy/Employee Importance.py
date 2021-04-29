#Leetcode 690. Employee Importance

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
        d = {}
        
        for emp in employees:
            d[emp.id] = emp
        
        ans = 0
        queue = deque()
        queue.append(id)
        
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                empId = queue.popleft()
                emp = d[empId]
                ans += emp.importance
                for i in emp.subordinates:
                    queue.append(i)
        return ans
                