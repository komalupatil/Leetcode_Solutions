#Leetcode 47. Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        buffer = [] 
        self.dfs(nums, buffer, seen, result)
        return result
    
    def dfs(self, nums, buffer, seen, result):
        if len(buffer) == len(nums):
            result.append(buffer[:])
            return
        
        visited = set()
        for i in range(len(nums)):
            if i not in seen and nums[i] not in visited:
                seen.add(i)
                visited.add(nums[i])
                buffer.append(nums[i])
                self.dfs(nums, buffer, seen, result)
                seen.remove(i)
                buffer.pop()