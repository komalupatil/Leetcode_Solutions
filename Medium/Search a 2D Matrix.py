#Leetcode 74. Search a 2D matrix

#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.

#how to find midElement is imp here, 
#remember the example of finding the position of 11th person if have to arrange 10 ppl in a row of 4s

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        columnSize = len(matrix[0])
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while (left <= right):
            
            mid = left + (right-left)//2
            midElement = matrix[mid//columnSize][mid%columnSize]
            #to find the position of midElement in the matrix and element at that position
        
            if (midElement == target):
                return True
            elif midElement > target:
                right = mid - 1
            else: 
                left = mid + 1
        return False
