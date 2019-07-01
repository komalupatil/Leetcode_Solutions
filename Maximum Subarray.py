class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], nums[i] + sum)
            max_sum = max(sum, max_sum)
        return max_sum