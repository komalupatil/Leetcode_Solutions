#leetcode 53
#o(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxEndingSoFar = nums[0]
        maxGlobal =nums[0]
        for i in range(1,len(nums)):
            maxEndingSoFar = max(nums[i], maxEndingSoFar + nums[i])
            maxGlobal = max(maxEndingSoFar, maxGlobal)
        return maxGlobal
