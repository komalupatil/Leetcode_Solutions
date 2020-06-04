#Leetcode 240. Search a 2D Matrix II

#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.

#Solution

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        m = len(matrix)    #rowlength
        n = len(matrix[0])   #columnlength
        
        row = 0
        column = n -1
        
        while (row < m and column >= 0):
            
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            else:
                row +=1
        return False
            