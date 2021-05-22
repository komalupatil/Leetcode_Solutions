#Leetcode 90. Subsets II

class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        buffer = []
        start = 0
        self.dfs(nums, start, buffer, result)
        return result
    
    def dfs(self, nums, start, buffer, result):
        result.append(buffer[:])
        visited = set()
        
        for i in range(start, len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                buffer.append(nums[i])
                self.dfs(nums, i+1, buffer, result)
                buffer.pop()

class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        buffer = []
        start = 0
        self.dfs(nums, start, buffer, result)
        return result
    
    def dfs(self, nums, start, buffer, result):
        result.append(buffer[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            buffer.append(nums[i])
            self.dfs(nums, i+1, buffer, result)
            buffer.pop()