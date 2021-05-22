#Leetcode 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        buffer = []
        start = 0
        self.dfs(nums, start, buffer, result)
        return result
    
    def dfs(self,nums, start, buffer, result):
        result.append(buffer[:])
        
        for i in range(start, len(nums)):
            buffer.append(nums[i])
            self.dfs(nums, i+1, buffer, result)
            buffer.pop()