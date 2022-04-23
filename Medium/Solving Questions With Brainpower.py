#Leetcode 2140. Solving Questions With Brainpower

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for i in range(len(questions))]
        
        return self.helper(0, questions, dp)
    
    def helper(self, index, questions, dp):
        
        if index >= len(questions):
            return 0
        
        if dp[index] != 0:
            return dp[index]
        
        choose = questions[index][0] + self.helper(index+questions[index][1]+1, questions, dp)
        unchoose = self.helper(index+1, questions, dp)
        dp[index] = max(choose, unchoose)
        
        return dp[index]