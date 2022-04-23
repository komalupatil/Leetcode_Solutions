#Leetcode 2139. Minimum Moves to Reach Target Score 

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        
        if maxDoubles == 0:
            return target -1
        
        result = 0
        while target > 1:
            if target %2 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                result += 1
                target = target //2
            elif maxDoubles == 0:
                result += target - 1
                target = 1
            else:
                target -= 1
                result += 1
        
        return result