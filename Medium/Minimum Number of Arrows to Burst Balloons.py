#Leetcode 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points = sorted(points, key = lambda x: x[1])
        arrows = 1
        end = points[0][1]
        
        for i in range(len(points)):
            if points[i][0] > end:
                arrows +=1
                end = points[i][1]
        return arrows