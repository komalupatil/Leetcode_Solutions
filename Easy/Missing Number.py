class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in nums:
                return number