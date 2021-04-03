#leetcode 1. Two Sum

#solution1

class Solution:
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


#solution2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return (d[m], i)
            else:
                d[n] = i

#solution3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x= target - nums[i]
            if x in d.keys():
                return (d[x], i)
            else:
                d[nums[i]] = i

