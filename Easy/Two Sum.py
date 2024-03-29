#Leetcode 1. Two Sum

class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i])+nums[j] == target:
                    return (i, j)

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return (d[m], i)
            else:
                d[n] = i


