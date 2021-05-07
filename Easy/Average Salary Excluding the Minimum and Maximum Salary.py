#Leetcode 1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution1:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        total = 0
        for i in range(1, len(salary)-1):
            total += salary[i]
        return total/(len(salary)-2)

class Solution2:
    def average(self, salary: List[int]) -> float:
        minS = float('inf')
        maxS = float('-inf')
        total = 0
        for i in range(len(salary)):
            total += salary[i]
            minS = min(minS, salary[i])
            maxS = max(maxS, salary[i])
        return (total-minS-maxS)/(len(salary)-2)