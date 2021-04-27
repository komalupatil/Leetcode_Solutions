#Leetcode 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]* (len(gain)+1)
        
        result[0] = 0
        result[1] = gain[0]
        
        for i in range(1, len(gain)):
            result[i+1] = result[i] + gain[i]
        
        return max(result)