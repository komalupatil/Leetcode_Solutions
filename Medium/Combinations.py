#Leetcode 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        buffer = []
        i = 1
        self.dfs(i,n, k, buffer, result)
        return result
    
    def dfs(self, i, n, k, buffer, result ):
        if len(buffer) == k:
            result.append(buffer[:])
            return
        for j in range(i, n+1):
            buffer.append(j)
            self.dfs(j+1, n, k, buffer, result)
            buffer.pop()