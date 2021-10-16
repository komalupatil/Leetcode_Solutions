#Leetcode 934. Shortest Bridge

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        found = False
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.dfs(grid,i,j,m,n,queue)
                    found = True
                    break
            if found:
                break
    
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            size = len(queue)
            level = []
            while(size):
                temp = queue.pop()
                size-=1
                x, y = temp[0], temp[1]
                for dx, dy in dirs:
                    tx = x+dx
                    ty = y+dy
                    if tx<0 or ty<0 or tx>=m or ty>=n or grid[tx][ty]==2:
                        continue
                    if grid[tx][ty]==1:
                        return steps
                    grid[tx][ty]=2
                    level.append((tx, ty))
            steps+=1
            queue = level
        return -1 
    
    
        
    def dfs(self,grid,i,j,m,n,queue):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
            return
        
        grid[i][j] = 2
        
        queue.append((i,j))
        self.dfs(grid, i+1, j, n, m, queue)
        self.dfs(grid, i-1, j, n, m, queue)
        self.dfs(grid, i, j+1, n, m, queue)
        self.dfs(grid, i, j-1, n, m, queue)