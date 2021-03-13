#Leetcode 217. Contains Duplicate

#Solution1

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


#Solution2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for num in nums:
            d[num] = d.get(num,0)+1
        for key in d:
            if d[key] > 1:
                return True
        return False

