#Leetcode 1344. Angle Between Hands of a Clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        min_deg = minutes * 6.0
        hour_deg = hour*30 + minutes * 0.5
        
        return min (abs(hour_deg - min_deg), 360-abs(hour_deg - min_deg))
    