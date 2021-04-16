#Leetcode 739. Daily Temperatures

#Solution - Monotonic Stack
# build a decreasing stack while finding next greater/larger element
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 0:
            return [0]
        
        nextWarmerTemp = [0] * len(T)
        stack = []
        
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                index = stack.pop()
                nextWarmerTemp[index] = i - index
            stack.append(i)
        return nextWarmerTemp