#leetcode 136 - single number 
#using XOR logic
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0 
        for i in range(len(nums)):
            sum = sum ^ nums[i]
        return sum
