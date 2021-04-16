#Leetcode

#Solution - monotonic stack

#find min left index while doing increasing mono stack from start
#find max right index while doing decreasing mono stack from end
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        left = len(nums)
        stack = []
        #monotonically increasing stack
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        
        right = 0
        stack = []
        #Monotonically decreasing stack
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)   
        if right-left >0:
            return right - left + 1
        return 0