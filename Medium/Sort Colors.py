#Leetcode 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        i = 0
        
        while(i<=right):
            color = nums[i]
            if color ==0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                i +=1
                left +=1
                
            elif color == 2:
                temp = nums[right]
                nums[right] = nums[i]
                nums[i] = temp
                right -=1
                
            elif color == 1:
                i +=1