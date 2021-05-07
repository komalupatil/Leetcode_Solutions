#Leetcode 217. Contains Duplicate

class Solution1:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for num in nums:
            d[num] = d.get(num,0)+1
        for key in d:
            if d[key] > 1:
                return True
        return False

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for num in nums:
            if num in d:
                return True
            d[num] = 0
        return False

