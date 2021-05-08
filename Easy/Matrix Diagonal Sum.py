#Leetcode 1572. Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        mid = len(mat)//2
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    result += mat[i][j]
                if i+j == len(mat[0])-1:
                    result += mat[i][j]
        if len(mat)%2 == 1:
            result -= mat[mid][mid]
        return result