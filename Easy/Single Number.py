#leetcode 136 - single number 
#using XOR logic
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result
