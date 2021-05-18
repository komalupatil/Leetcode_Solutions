#Leetcode 62. Unique Paths

class Solution1:
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

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]