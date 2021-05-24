#Leetcode 198. House Robber

class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
        return dp[-1]
        

class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums == None:
            return 0
        
        dp1, dp2 = 0, 0
        
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)          
        return dp2 