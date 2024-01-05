# Leetcode 42. Trapping Rain Water

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        total_water_trapped = 0
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])
        for j in range(n-2, -1, -1):
            rightMax[j] = max(rightMax[j+1], height[j])
    
        for k in range(0, len(height)):
            equi = min(leftMax[k], rightMax[k])
            water = equi - height[k]
            total_water_trapped += water
        return total_water_trapped



        #   0, 1 ,0, 2, 1, 0, 1, 3, 2, 1, 2, 1
        # l 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3
        # r 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1
        # w 0  0. 1. 0. 1. 2. 1  0. 0  1. 0. 0
    


"""
Two Pointer method
"""
class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        n = len(height)
        maxLeft = 0
        maxRight = 0
        left = 0
        right = n - 1
        totalWater = 0
    
        while left <= right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:
                totalWater += maxLeft - height[left]
                left += 1
            else:
                totalWater += maxRight - height[right]
                right -= 1 
        return totalWater