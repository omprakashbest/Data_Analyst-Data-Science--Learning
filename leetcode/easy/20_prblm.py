"""
Design Parking System :

Design a parking system for a parking lot. the parking lot has three kinds of parking spaces: big, median
and small , with a fixed number of slots of each size.

"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small] # index = 0, 1, 2

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        return False 

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)