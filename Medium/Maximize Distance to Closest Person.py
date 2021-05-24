#Leetcode 849. Maximize Distance to Closest Person

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat = None
        dist = float('-inf')
        
        for indx in range(len(seats)):
            if seats[indx] == 1:
                if prev_seat == None:
                    dist = indx
                else:
                    dist = max(dist, (indx - prev_seat)//2)
                prev_seat = indx
                
        dist = max(dist, len(seats)-1-prev_seat)
        
        return dist