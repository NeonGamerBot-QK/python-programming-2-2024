import math
class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return self.__abs__() > 0
    def __add__(self):
        return self.x + self.y
    def __mul__(self):
        # IDK
        return self.x * self.y