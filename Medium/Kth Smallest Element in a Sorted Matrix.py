#Leetcode 378. Kth Smallest Element in a Sorted Matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        matrix_min = matrix[0][0]
        matrix_max = matrix[n-1][n-1]
        
        while matrix_min < matrix_max:
            mid = (matrix_max + matrix_min)//2
            if self.count(mid, matrix) < k:
                matrix_min = mid + 1
            else:
                matrix_max = mid
        return matrix_max
    def count(self, i, matrix):
        n = len(matrix)
        row = 0
        col = n-1
        count = 0
        while row < n and col >= 0:
            if matrix[row][col] <= i:
                count += col + 1
                row += 1
            else:
                col -= 1
        return count