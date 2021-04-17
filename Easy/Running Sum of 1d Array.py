#Leetcode 1480. Running Sum of 1d Array

#Solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
#Solution2

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumN = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + sumN
            sumN = nums[i]
        return nums