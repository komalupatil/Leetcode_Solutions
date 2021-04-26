#Leetcode 1351. Count Negative Numbers in a Sorted Matrix

#Solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = 0
        col = len(grid[0])-1
        
        totalRows = len(grid)
        count = 0
        
        while row < totalRows and col >=0:
            if grid[row][col] < 0:
                count += totalRows - row
                col -= 1
            else:
                row += 1
        return count