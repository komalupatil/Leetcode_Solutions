#Leetcode 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        
        stack.append(-1)
        maxArea = 0
        for i in range(len(heights)+1):
            val = heights[i] if i != len(heights) else 0
            while stack[-1] != -1 and heights[stack[-1]] >= val:
                rm = i
                h = heights[stack.pop()]
                lm = stack[-1]
                maxArea = max(maxArea, h*(rm-lm-1))
            stack.append(i)
        return maxArea