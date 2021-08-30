#Leetcode 200. Number of Islands
#https://yangshun.github.io/tech-interview-handbook/algorithms/graph/

#Solution 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        noOfIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    noOfIslands +=1
        return noOfIslands
        
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j] != '1':
            return 
        
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)