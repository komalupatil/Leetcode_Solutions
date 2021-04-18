#Leetcode 643. Maximum Average Subarray I

#Solution - sliding window pattern
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1 and k==1:
            return nums[0]
        windowStart = 0
        maxSum = float('-inf')
        windowSum = 0.0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k-1:
                maxSum = max(maxSum, windowSum)
                windowSum = windowSum - nums[windowStart]
                windowStart +=1
                
        maxAvg = maxSum/k
        return maxAvg
                