#Leetcode 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        R = len(self.board)
        if R <= 2:
            return
        C = len(self.board[0])
        if C <= 2:
            return
        
        for i in range(R):
            for j in range(C):
                if self.board[i][j] == "O" and (i == 0 or j == 0 or i == R-1 or j == C-1):
                    self.dfs(i,j)
        for i in range(R):
            for j in range(C):
                if self.board[i][j] == "O":
                    self.board[i][j] = "X"
                elif self.board[i][j] == "A":
                    self.board[i][j] = "O"
                    
        
    def dfs(self,i,j):
        if i >= 0 and i < len(self.board) and j >= 0 and j<len(self.board[0]) and self.board[i][j] == "O":
            self.board[i][j] = "A"
            self.dfs(i-1, j)
            self.dfs(i+1, j)
            self.dfs(i, j-1)
            self.dfs(i, j+1)