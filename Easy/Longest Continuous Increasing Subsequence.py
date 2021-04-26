#Leetcode 674. Longest Continuous Increasing Subsequence

#Solution - sliding window
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        windowStart = 0
        maxLength = 0

        for windowEnd in range(1, len(nums)):
            if nums[windowEnd] <= nums[windowEnd-1]:
                windowStart = windowEnd
            maxLength = max(maxLength, windowEnd - windowStart + 1)     
             
        return maxLength