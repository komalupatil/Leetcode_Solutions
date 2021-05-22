#Leetcode 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        buffer = [] 
        seen = set()
        self.dfs(nums, buffer, seen, result)
        return result
    
    def dfs(self, nums, buffer, seen, result):
        if len(buffer) == len(nums):
            result.append(buffer[:])
            return
        for i in range(len(nums)):
            if i not in seen:
                seen.add(i)
                buffer.append(nums[i])
                self.dfs(nums, buffer, seen, result)
                seen.remove(i)
                buffer.pop()