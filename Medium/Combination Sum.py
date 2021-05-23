#Leetcode 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        buffer = []
        addition = 0
        i = 0
        self.dfs(i, candidates, target, addition, buffer, result)
        return result
    
    def dfs(self, start, candidates, target, addition, buffer, result):
        if addition == target:
            result.append(buffer[:])
            return 
        
        if addition > target:
            return
        
        for j in range(start, len(candidates)):
            addition += candidates[j]
            buffer.append(candidates[j])
            self.dfs(j, candidates, target, addition, buffer, result)
            buffer.pop()
            addition -= candidates[j]