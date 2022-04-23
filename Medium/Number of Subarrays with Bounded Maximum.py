#Leetcode 795. Number of Subarrays with Bounded Maximum

# refer https://www.youtube.com/watch?v=My3pobBPtbA&t=11s
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        startIndex = 0
        endIndex = 0
        
        n = len(nums)
        ans = 0
        prevCount = 0
        
        while endIndex < n:
            if left <= nums[endIndex] and nums[endIndex] <= right:
                prevCount = endIndex - startIndex +1
                ans += prevCount
            elif nums[endIndex] < left:
                ans += prevCount
            else:
                startIndex = endIndex + 1
                prevCount = 0
            endIndex += 1
        
        return ans