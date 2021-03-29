#Leetcode 300. Longest Increasing Subsequence

#Solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        
        T = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if T[j]+1 > T[i]:
                        T[i] = T[j]+1
        longest = 0
        
        for i in range(len(T)):
            longest = max(longest, T[i])
        return longest