#Leetcode 238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums) #left array
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right = 1 #right product
        for i in range(len(nums)-2, -1, -1):
            right = right * nums[i+1]
            left[i] = left[i] * right
        return left
