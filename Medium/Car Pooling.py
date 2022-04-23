#Leetcode 1094. Car Pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        newList = []
        
        for trip in trips:
            newList.append([trip[1], 1, trip[0]])
            newList.append([trip[2], 0, trip[0]])
        newList.sort()
        
        curr = 0
        for lst in newList:
            if lst[1] == 1:
                curr += lst[2]
            else:
                curr -= lst[2]
            if curr > capacity:
                return False
        return True