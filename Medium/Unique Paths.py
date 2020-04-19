#Leetcode 62. Unique Paths

#Solution - using DP - similar to Minimum path sum

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1 for _ in range(n)]for _ in range(m)]
        
        dp[0][0] = 1
        
        for j in range(1,n):
            dp[0][j] = 1
            
        for i in range(1,m):
            dp[i][0] = 1
        
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
        return dp[-1][-1]