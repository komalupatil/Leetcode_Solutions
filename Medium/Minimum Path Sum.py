#Leetcode 64. Minimum Path Sum

class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n= len(grid[0])
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        #dp = [[1*len(grid)]*len(grid[0])]
        
        dp[0][0] = grid[0][0]
        
        #first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        #first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
                
                
        return dp[len(grid)-1][len(grid[0])-1]

#Bottom up approach DP
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        result = self.helper(grid, m-1, n-1, dp)
        
        return result
        
    def helper(self, grid, m, n, dp):
        if m == 0 and n == 0:
            return grid[m][n]
        
        if m<0 or n<0:
            return float('inf')
        
        if dp[m][n] != 0:
            return dp[m][n]
        
        up = self.helper(grid, m-1, n, dp)
        left = self.helper(grid, m, n-1, dp)
        
        result = min(up,left) + grid[m][n]
        
        dp[m][n] = result
        
        return dp[m][n]