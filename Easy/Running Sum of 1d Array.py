#Leetcode 1480. Running Sum of 1d Array

class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumN = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + sumN
            sumN = nums[i]
        return nums