#Leetcode 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = []
        res.append([1])
        res.append([1,1])
        for i in range(2, numRows):
            row = [1]
            j = 1
            while j < i:
                row.append(res[i-1][j-1]+res[i-1][j])
                j+=1
            row.append(1)
            res.append(row)
        return res