#Leetcode 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = max(self.dfs(grid,i,j), count)
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        
        next_row = self.dfs(grid,i+1,j)
        prev_row = self.dfs(grid,i-1,j)
        next_col = self.dfs(grid,i,j+1)
        prev_col = self.dfs(grid,i,j-1)
        
        return 1 + next_row + prev_row + next_col + prev_col