#Leetcode 448. Find All Numbers Disappeared in an Array

#SOlution using cyclic sort

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result
            
