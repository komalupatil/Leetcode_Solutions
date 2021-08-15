#Leetcode 1603. Design Parking System

#Solution1
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


#Solution2
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = {1:big, 2:medium, 3:small}
        

    def addCar(self, carType: int) -> bool:
        if self.park[carType]:
            self.park[carType] -= 1
            return True
        return False
            

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)