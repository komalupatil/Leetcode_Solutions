#Leetcode 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        buffer = []
        addition = 0
        start  = 0
        self.dfs(start, candidates, target, addition, buffer, result)
        return result
    
    def dfs(self, i, candidates, target, addition, buffer, result):
        if addition == target:
            result.append(buffer[:])
            return
        
        if addition > target:
            return
        
        visited = set()
        for j in range(i, len(candidates)):
            if candidates[j] not in visited:
                visited.add(candidates[j])
                addition += candidates[j]
                buffer.append(candidates[j])
                self.dfs(j+1, candidates, target, addition, buffer, result)
                buffer.pop()
                addition -= candidates[j]