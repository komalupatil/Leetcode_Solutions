#Leetcode 1232. Check If It Is a Straight Line

#Solution


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        (x0, y0), (x1,y1) = coordinates[:2]
        for x, y in coordinates:
            #in 3 pts given, 
            # slope between 1st and 2nd and 2nd 
            # and 3rd must be equal to be a straight line
            if (y1-y0)*(x-x1) != (y-y1)*(x1-x0):
                return False
        return True
