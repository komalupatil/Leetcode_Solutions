#Leetcode 503. Next Greater Element II

#Solution - Monotonic Stack

# build a decreasing stack while finding next greater/larger element
# for circular array, loop through 2 times len(array) and push i%len(array) to stack always

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return [0]
        
        stack = [] # decreasing stack build
        nextGreaterElements = [-1] * len(nums) #result array
        n = len(nums)
        
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                nextGreaterElements[stack.pop()] = nums[i%n]
            stack.append(i%n)
            
        return nextGreaterElements