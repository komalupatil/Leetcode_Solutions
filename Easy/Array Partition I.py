#Leetcode 561. Array Partition I

#sort the array so that alternate elements will be min of the addition of its adjecent element and all those alternates element addition will be the min sum
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        for i in range(0,len(nums), 2):
            min_sum = min_sum + nums[i]
        return min_sum
