#leetcode 643
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1 and k==1:
            return nums[0]
        windowStart = 0
        maxSum = float('-inf') #values in nums can be negative so take min Sum (min int value)
        windowSum = 0.0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k-1:
                maxSum = max(maxSum, windowSum)
                windowSum = windowSum - nums[windowStart]
                windowStart +=1
                
        maxAvg = maxSum/k #max avg will be of the max sum so need to calculate avg for each max sum
        return maxAvg
