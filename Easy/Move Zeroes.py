#Leetcode 283. Move Zeroes

#Solution 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        return nums


#Solution 2


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                right +=1
            else:
                left +=1
                nums[left] = nums[right]
                right +=1 
        for i in range(left+1, len(nums)):
            nums[i] = 0
        return nums