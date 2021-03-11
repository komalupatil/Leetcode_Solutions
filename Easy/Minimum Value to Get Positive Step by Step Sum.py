#Leetcode 1413. Minimum Value to Get Positive Step by Step Sum

#Solution

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        minPrefixSum = 0
        for num in nums:
            s += num
            minPrefixSum = min(s, minPrefixSum)
        return 1-minPrefixSum