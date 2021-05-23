#Leetcode 216. Combination Sum III

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        buffer = []
        start = 1
        addition = 0
        self.dfs(start, addition, n, k, buffer, result)
        return result
    
    def dfs(self, i, addition, n, k, buffer, result):
        if addition == n and len(buffer) == k:
            result.append(buffer[:])
            return
        if addition > n or len(buffer) > k:
            return
        
        for j in range(i, 10):
            buffer.append(j)
            addition += j
            self.dfs(j+1, addition, n, k, buffer, result)
            buffer.pop()
            addition -= j