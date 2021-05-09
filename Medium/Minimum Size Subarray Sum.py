#Leetcode 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        windowStart = 0
        windowSum = 0.0
        minLength = float('inf')
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            print("windowSum ", windowSum)
            while(windowSum >= s):
                minLength = min(minLength, windowEnd-windowStart+1)
                print(minLength)
                windowSum = windowSum - nums[windowStart]
                windowStart += 1
                
        if minLength == float('inf'): #for conditions like s=3, [1,1] where it wont go into while loop and minLength will be infinite
            return 0
        else:
            
            return minLength
