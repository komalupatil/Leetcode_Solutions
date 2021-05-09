#Leetcode 54. Spiral Matrix

class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while l < r and u < d:
            ans.extend([matrix[u][j] for j in range(l, r)])
            ans.extend([matrix[i][r] for i in range(u, d)])
            ans.extend([matrix[d][j] for j in range(r, l, -1)])
            ans.extend([matrix[i][l] for i in range(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            ans.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in range(l, r + 1)])
        return ans

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        colStart = 0
        rowLength = len(matrix) -1
        colLength = len(matrix[0]) - 1
        
        result = []
        while rowStart <= rowLength and colStart <= colLength:
            for i in range(colStart, colLength+1):
                #print("i = ", i)
                result.append(matrix[rowStart][i])

            rowStart += 1

            for j in range(rowStart, rowLength+1):
                #print("j = ", j)
                result.append(matrix[j][colLength])

            colLength -= 1

            if rowStart <= rowLength:
                for k in range(colLength, colStart-1, -1):
                    #print("k = ", k)
                    result.append(matrix[rowLength][k])

                rowLength -= 1

            if colStart <= colLength:

                for l in range(rowLength, rowStart-1, -1):
                    #print("l = ", l)
                    result.append(matrix[l][colStart])

                colStart += 1
        
        return result