class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_total = 0
        for i in range(len(nums)):
            list_total = nums[i] + list_total
        total = ((len(nums)+1)*(len(nums)))/2
        missing_num = total - list_total
        return int(missing_num)