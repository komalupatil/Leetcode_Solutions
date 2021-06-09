#Leetcode 289. Game of Life

#o(mn) - extra space solution
class Solution1:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        neighbors = [(1,0), (1,1), (0,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]
        
        rows = len(board)
        cols = len(board[0])
        
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    
                    if (r < rows and r>=0) and (c < cols and c>=0) and (copy_board[r][c] == 1):
                        live_neighbors += 1
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
            
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

#o(1) space solution
#use -1 value for the cell whose value changed from 1 to 0 and use 2 as value for cell whose value changed from 0 to 1. and use these values to compute result.
class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        neighbors = [(1,0), (1,1), (0,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]
        
        rows = len(board)
        cols = len(board[0])
        
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    
                    if (r < rows and r>=0) and (c < cols and c>=0) and (abs(board[r][c]) == 1):
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
            
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] >0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0