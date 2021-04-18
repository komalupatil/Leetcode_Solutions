#Leetcode 268. Missing Number

#solution1
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

#solution2
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            else:
                i += 1
        return i

#solution3
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


#Solution4 using cyclic sort (time complexity o(n) and space complexity o(1))
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
