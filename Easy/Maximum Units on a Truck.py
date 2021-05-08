#Leetcode 1710. Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for box, units in boxTypes:
            if truckSize >= box:
                res += box * units
                truckSize -= box
            else:
                res += truckSize * units
                break
        return res